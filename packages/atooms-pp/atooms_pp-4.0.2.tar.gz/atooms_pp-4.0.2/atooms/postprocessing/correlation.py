# This file is part of atooms
# Copyright 2010-2024, Daniele Coslovich

"""Base correlation function."""

# TODO: pp should provide a results dict that packs grid and values e.g. like
#  {'F_s(k,t)': [fskt.grid, fskt.value]}
#  {'MSD(t)': [msd.grid, msd.value]}
#
# For partials I would do
#  {'F_s^{1-1}(k,t)': [fskt.partial[('1', '1')].grid, fskt.partial[('1', '1')].value]}
#  {'MSD_1(t)': [msd.partial['1'].grid, fskt.partial['1'].value]}
#
# It would be similar for analysis
#  {'tau_s(k)': [fskt.grid[0], fskt.analysis.tau]}
#  {'D': msd.diffusion_coefficient}
#
# It should be possible to just update these dicts without overriding existing keys.
# So results could be a property of Correlation, which returns at runtime.
# One exception could be "artifacts". We want to collect all artifacts there
# when updating the dicts. So we need a custom update that allows some entries to be merged
# for instance by summing their values.

import os
import logging
from collections import defaultdict
import numpy

from atooms.trajectory import Trajectory
from atooms.trajectory.decorators import Unfolded, fold
from atooms.trajectory.decorators import change_species
from atooms.system.particle import distinct_species
from atooms.core.utils import Timer, mkdir

from . import core
from .helpers import adjust_skip
from .progress import progress

__all__ = ['acf', 'gcf', 'gcf_offset', 'Correlation']

_log = logging.getLogger(__name__)

def acf(grid, skip, t, x):
    """
    Auto-correlation function <x(t)x(0)> of a time series x(t)

    The correlation is between `x[i0+i]` and `x[i0]`, where `i` is
    taken from the `grid` list and `i0` is a time origin. The average
    <...> is over the time origins. The time differences are
    calculated as `t[i0+i]-t[i0]`.

    :param grid: list of time indices `i` for which the correlation is computed
    :param skip: average every `skip` time origins
    :param t: times t[i]
    :param x: time series x[i]
    :returns: list of time differences, list of correlation function,
    list of number of time origins for each entry of the previou lists
    """
    cf = defaultdict(float)
    cnt = defaultdict(int)
    xave = numpy.average(x)
    for i in grid:
        for i0 in range(0, len(x)-i, skip):
            # Get the actual time difference
            dt = t[i0+i] - t[i0]
            cf[dt] += (x[i0+i]-xave) * (x[i0]-xave)
            cnt[dt] += 1

    # Return the ACF with the time differences sorted
    dt = sorted(cf.keys())
    return dt, [cf[ti] / cnt[ti] for ti in dt], cnt


def gcf(f, grid, skip, t, x):
    """
    Generalized auto-correlation function <f(x[i], x[i0])>

    Pass a function `f` to apply to the data at each frame.

    Exemple: mean square displacement.
    """
    # Calculate the correlation between time t(i0) and t(i0+i)
    # for all possible pairs (i0,i) provided by grid
    cf = defaultdict(float)
    cnt = defaultdict(int)
    for i in grid:
        # Note: len(x) gives x.shape[0]
        for i0 in progress(range(0, len(x)-i-1, skip)):
            # Get the actual time difference
            dt = t[i0+i] - t[i0]
            cf[dt] += f(x[i0+i], x[i0])
            cnt[dt] += 1

    # Return the ACF with the time differences sorted
    dt = sorted(cf.keys())
    return dt, [cf[ti] / cnt[ti] for ti in dt], [cnt[ti] for ti in dt]


def gcf_offset(f, grid, skip, t, x):
    """
    Generalized auto-correlation function <f(x[i], x[i0])> using a grid with offsets

    Pass a function `f` to apply to the data `x` at each frame.

    Exemple: mean square displacement.
    """
    # Calculate the correlation between time t(i0) and t(i0+i)
    # for all possible pairs (i0,i) provided by grid
    cf = defaultdict(float)
    cnt = defaultdict(int)
    # Standard calculation
    for off, i in progress(grid, total=len(grid)):
        for i0 in range(off, len(x)-i, skip):
            # Get the actual time difference
            dt = t[i0+i] - t[i0]
            cf[dt] += f(x[i0+i], x[i0])
            cnt[dt] += 1

    # Return the ACF with the time differences sorted
    dt = sorted(cf.keys())
    return dt, [cf[ti] / cnt[ti] for ti in dt]


def _subtract_mean(weight):
    mean = 0
    for current_field in weight:
        mean += current_field.mean()
    mean /= len(weight)
    for current_field in weight:
        current_field -= mean
    return weight


def _is_iterable(maybe_iterable):
    try:
        iter(maybe_iterable)
    except TypeError:
        return False
    else:
        return True


class Correlation:
    """
    Base class for correlation functions.

    The correlation function is calculated for the trajectory `trj`. This can be:

    - an object implementing the atooms `Trajectory` interface
    - the path to a trajectory file in a format recognized by atooms

    A correlation function A(x) is defined over a grid of real
    entries {x_i} given by the list `grid`. To each entry of the grid,
    the correlation function has a corresponding value A_i=A(x_i). The
    latter values are stored in the `value` list.

    Correlation functions that depend on several variables, A(x,y,...)
    must provide a list of grids, one for each variable. The order is
    one specified by the `symbol` class variable, see below.

    The correlation function A is calculated as a statistical average
    over several time origins in the trajectory `trj`. The `norigins`
    variable can be used to tune the number of time origins used to
    carry out the average. `norigins` can take the following values:

    - `norigins=-1`: all origins are used
    - an integer >= 1: use only `n_origins` time origins
    - a float in the interval (0,1): use only a fraction `norigins` of frames as time origins
    - `None`: a heuristics is used to keep the product of steps times particles constant

    Subclasses must provide a symbolic expression of the correlation
    function through the `symbol` class variable. The following
    convention is used: if a correlation function A depends on
    variables x and y, then `symbol = 'A(x,y)'`.

    The `variables` variable allow subclasses to access a list of 2d
    numpy arrays with particles coordinates via the following private
    variables:

    - if `nbodies` is 1: `self._pos` for positions, `self._vel` for
    velocities, `self._unf_pos` for PBC-unfolded positions

    - if `nbodies` is 2, an additional suffix that take values 0 or 1
    is added to distinguish the two sets of particles,
    e.g. `self._pos_0` and `self._pos_1`
    """

    nbodies = 1
    """
    Class variable that controls the number of bodies, i.e. particles,
    associated to the correlation function. This variable controls the
    internal arrays used to compute the correlation, see `variables`.
    """
    static = False
    """
    Turn this to `True` is the correlation function is static,
    i.e. not time-dependent. This may enable some optimizations.
    """
    symbol = ''
    """Example: fskt"""
    short_name = ''
    # TODO: rename name
    """Example: F_s(k,t)"""
    long_name = ''
    # TODO: rename description
    """Example: Self intermediate scattering function"""
    variables = ['pos', 'pos-unf', 'vel']
    """
    List of strings or string among ['pos', 'pos-unf', 'vel']. It
    indicates which variables should be read from the trajectory file.
    They will be available as self._pos, self._pos_unf, self._vel.
    """
    _symmetric = True
    """
    If nbodies>1, a symmetric correlation function is invariant under
    the exchange between _pos_0 and _pos_1. In that case, _symmetric
    is True.
    """

    def __init__(self, trj, grid, output_path=None, norigins=None, fix_cm=False):
        """
        The `output_path` instance variable is used to define the
        output files by interpolating the following instance variables:

        - `symbol`
        - `short_name`
        - `long_name`
        - `tag`
        - `tag_description`
        - `trajectory`

        The default is defined by core.pp_output_path, which currently
        looks like '{trajectory.filename}.pp.{symbol}.{tag}'
        """
        # Accept a trajectory-like instance or a path to a trajectory
        if isinstance(trj, str):
            self.trajectory = Trajectory(trj, mode='r', fmt=core.pp_trajectory_format)
        else:
            self.trajectory = trj
        self._fix_cm = fix_cm
        self._unfolded = None
        self.grid = grid
        self.values = []
        self.origins = []
        self.tag = ''
        self.tag_description = 'the whole system'
        self._analysis = {}
        self._trajectory_path = self.trajectory.filename
        if self._trajectory_path is None:
            self.output_path = None
        else:
            self.output_path = output_path if output_path is not None else core.pp_output_path
        self.skip = adjust_skip(self.trajectory, norigins)

        # Callbacks
        self._cbk = []
        self._cbk_args = []
        self._cbk_kwargs = []

        # Lists for one body correlations
        # TODO: group these vars better, there could be a single self._data dict
        # then self._data_0['pos'], self._data_0['vel'], ...
        self._pos = []
        self._vel = []
        self._ids = []
        self._pos_unf = []

        # Lists for two-body correlations
        self._pos_0, self._pos_1 = [], []
        self._vel_0, self._vel_1 = [], []
        self._ids_0, self._ids_1 = [], []
        self._pos_unf_0, self._pos_unf_1 = [], []

        # Weights
        self._weight = None
        self._weight_0, self._weight_1 = None, None
        self._weight_field = None
        self._weight_fluctuations = False

    def __str__(self):
        return '{} at <{}>'.format(self.long_name, id(self))

    # @property
    # def grid(self):
    #     if self._grid is None:
    #         return numpy.array([])
    #     return numpy.asarray(self._grid)

    # @grid.setter
    # def grid(self, val):
    #     self._grid = val

    # Note: value is deprecated in favor of values
    @property
    def value(self):
        return self.values

    @value.setter
    def value(self, val):
        self.values = val

    def add_weight(self, trajectory=None, field=None, fluctuations=False):
        """
        Add weight from the given `field` in `trajectory`

        If `trajectory` is `None`, `self.trajectory` will be used and
        `field` must be a particle property.

        If `field` is `None`, `trajectory` is assumed to be a path an
        xyz trajectory and we use the data in last column as a weight.

        If both `field` and `trajectory` are `None` the function
        returns immediately and the weight is not set.

        The optional `fluctuations` option subtracts the mean,
        calculated from the ensemble average, from the weight.
        """
        if trajectory is None and field is None:
            return

        self._weight = []
        self._weight_fluctuations = fluctuations

        # Guessing the field from the last column of an xyz file is
        # not supported anymore
        if field is None:
            raise ValueError('provide field to use as weight')
        else:
            self._weight_field = field

        # By default we use the same trajectory as for the variables
        if trajectory is None:
            self._weight_trajectory = self.trajectory
        else:
            self._weight_trajectory = trajectory
            # Copy over the field
            from .helpers import copy_field
            self.trajectory.add_callback(copy_field, self._weight_field, self._weight_trajectory)

        # Make sure the steps are consistent
        if self._weight_trajectory.steps != self.trajectory.steps:
            raise ValueError('inconsistency between weight trajectory and trajectory')

        # Modify tag
        fluct = 'fluctuations' if self._weight_fluctuations else ''
        self.tag_description += ' with {} {} field'.format(self._weight_field.replace('_', ' '), fluct)
        self.tag_description = self.tag_description.replace('  ', ' ')
        self.tag += '.{}_{}'.format(self._weight_field, fluct)
        self.tag.strip('_.')

    def add_filter(self, cbk, *args, **kwargs):
        """Add filter callback `cbk` along with positional and keyword arguments"""
        if len(self._cbk) > self.nbodies:
            raise ValueError('number of filters cannot exceed n. of bodies')
        self._cbk.append(cbk)
        self._cbk_args.append(args)
        self._cbk_kwargs.append(kwargs)

    def _setup_arrays(self):
        """
        Dump positions and/or velocities at different time frames as a
        list of numpy array.
        """
        # TODO: what happens if we call compute twice?? Shouldnt we reset the arrays?
        # Ensure variables is a list.
        # It may not be a class variable anymore after this
        if not isinstance(self.variables, list) and \
           not isinstance(self.variables, tuple):
            self.variables = [self.variables]

        # Setup arrays
        if self.nbodies == 1:
            self._setup_arrays_onebody()
            self._setup_weight_onebody()
        elif self.nbodies == 2:
            self._setup_arrays_twobody()
            self._setup_weight_twobody()

    def _setup_arrays_onebody(self):
        """
        Setup list of numpy arrays for one-body correlations.

        We also take care of dumping the weight if needed, see
        `add_weight()`.
        """
        # Local shortcut
        th = self.trajectory

        # We unfold the trajectory if variables requests it and
        # unfolded positions are not available in the trajectory, or
        # if we request folded positions with fixed center of mass
        if ('pos-unf' in self.variables and not hasattr(th[0].particle[0], 'position_unfolded')) or \
           ('pos' in self.variables and self._fix_cm):
            # We unfold the positions, caching the trajectory
            if self._unfolded is None:
                self._unfolded = Unfolded(self.trajectory, fixed_cm=self._fix_cm)
                # We must fold positions back in this case
                if 'pos' in self.variables:
                    self._unfolded.add_callback(fold)
            # Change the local shortcut to the unfolded trajectory
            th = self._unfolded

        # Read everything except unfolded trajectories
        if 'pos' in self.variables or 'vel' in self.variables or 'ids' in self.variables:
            ids = distinct_species(th[0].particle)
            for s in progress(th):
                # Apply filter if there is one
                if len(self._cbk) > 0:
                    s = self._cbk[0](s, *self._cbk_args[0], **self._cbk_kwargs[0])
                if 'pos' in self.variables:
                    self._pos.append(s.dump('pos'))
                if 'vel' in self.variables:
                    self._vel.append(s.dump('vel'))
                if 'ids' in self.variables:
                    _ids = s.dump('species')
                    _ids = numpy.array([ids.index(_) for _ in _ids], dtype=numpy.int32)
                    self._ids.append(_ids)

        # Read unfolded positions if requested
        if 'pos-unf' in self.variables:
            if hasattr(th[0].particle[0], 'position_unfolded'):
                # Unfolded positions are present in the trajectory
                for s in progress(th):
                    # Fixing the CM must be done explicitly using
                    # particle.position_unfolded because atooms.system
                    # methods work with particle.position
                    # TODO: can be revised with atooms 3.4.0
                    if self._fix_cm:
                        # Compute CM using unfolded positions, which is safe
                        cm = numpy.zeros_like(s.particle[0].position_unfolded)
                        mtot = 0.0
                        for p in s.particle:
                            cm += p.position_unfolded * p.mass
                            mtot += p.mass
                        cm /= mtot
                        # Subtract it
                        for p in s.particle:
                            p.position_unfolded -= cm
                    # Apply filter if there is one
                    # This must be done after the CM has been fixed
                    if len(self._cbk) > 0:
                        s = self._cbk[0](s, *self._cbk_args[0], **self._cbk_kwargs[0])
                    self._pos_unf.append(s.dump('particle.position_unfolded'))
            else:
                for s in progress(th):
                    # Apply filter if there is one
                    if len(self._cbk) > 0:
                        s = self._cbk[0](s, *self._cbk_args[0], **self._cbk_kwargs[0])
                    self._pos_unf.append(s.dump('pos'))

    def _setup_weight_onebody(self):
        """
        Setup list of numpy arrays for the weight, see `add_weight()`
        """
        if self._weight is None:
            return

        # Dump arrays of weights
        for s in progress(self.trajectory):
            # Apply filter if there is one
            # TODO: fix when weight trajectory does not contain actual particle info
            # It should be possible to link the weight trajectory to the trajectory
            # and return the trajectory particles with the weight
            if len(self._cbk) > 0:
                s = self._cbk[0](s, *self._cbk_args[0], **self._cbk_kwargs[0])
            current_weight = s.dump('particle.%s' % self._weight_field)
            self._weight.append(current_weight)

        # Subtract global mean
        if self._weight_fluctuations:
            _subtract_mean(self._weight)

    def _setup_weight_twobody(self):
        """
        Setup list of numpy arrays for the weight, see `add_weight()`
        """
        if self._weight is None:
            return

        self._weight = []
        self._weight_0 = []
        self._weight_1 = []

        # TODO: add checks on number of filters
        if len(self._cbk) <= 1:
            self._setup_weight_onebody()
            self._weight_0 = self._weight
            self._weight_1 = self._weight
            return

        # Dump arrays of weights
        for s in progress(self.trajectory):
            # Apply filters
            if len(self._cbk) == 2:
                s0 = self._cbk[0](s, *self._cbk_args[0], **self._cbk_kwargs[0])
                s1 = self._cbk[1](s, *self._cbk_args[1], **self._cbk_kwargs[1])
            self._weight_0.append(s0.dump('particle.%s' % self._weight_field))
            self._weight_1.append(s1.dump('particle.%s' % self._weight_field))

        # Subtract global mean
        if self._weight_fluctuations:
            _subtract_mean(self._weight_0)
            _subtract_mean(self._weight_1)

    def _setup_arrays_twobody(self):
        """Setup list of numpy arrays for two-body correlations."""
        if len(self._cbk) <= 1:
            self._setup_arrays_onebody()
            self._pos_0 = self._pos
            self._pos_1 = self._pos
            self._vel_0 = self._vel
            self._vel_1 = self._vel
            self._ids_0 = self._ids
            self._ids_1 = self._ids
            return

        if 'pos' in self.variables or 'vel' in self.variables or 'ids' in self.variables:
            ids = distinct_species(self.trajectory[0].particle)
            for s in progress(self.trajectory):
                s0 = self._cbk[0](s, *self._cbk_args[0], **self._cbk_kwargs[0])
                s1 = self._cbk[1](s, *self._cbk_args[1], **self._cbk_kwargs[1])
                if 'pos' in self.variables:
                    self._pos_0.append(s0.dump('pos'))
                    self._pos_1.append(s1.dump('pos'))
                if 'vel' in self.variables:
                    self._vel_0.append(s0.dump('vel'))
                    self._vel_1.append(s1.dump('vel'))
                if 'ids' in self.variables:
                    _ids_0 = s0.dump('species')
                    _ids_1 = s1.dump('species')
                    _ids_0 = numpy.array([ids.index(_) for _ in _ids_0], dtype=numpy.int32)
                    _ids_1 = numpy.array([ids.index(_) for _ in _ids_1], dtype=numpy.int32)
                    self._ids_0.append(_ids_0)
                    self._ids_1.append(_ids_1)

        # Dump unfolded positions if requested
        if 'pos-unf' in self.variables:
            for s in progress(Unfolded(self.trajectory)):
                s0 = self._cbk[0](s, *self._cbk_args[0], **self._cbk_kwargs[0])
                s1 = self._cbk[1](s, *self._cbk_args[1], **self._cbk_kwargs[1])
                self._pos_unf_0.append(s0.dump('pos'))
                self._pos_unf_1.append(s1.dump('pos'))

    def compute(self):
        """
        Compute the correlation function.

        It wraps the _compute() method implemented by subclasses.
        This method sets the `self.grid` and `self.values` variables,
        which are also returned.
        """
        _log.info('setup arrays for %s', self.tag_description)
        t = [Timer(), Timer()]
        t[0].start()
        self._setup_arrays()
        t[0].stop()

        _log.info('computing %s for %s', self.long_name, self.tag_description)
        _log.info('using %s time origins out of %s',
                  len(range(0, len(self.trajectory), self.skip)),
                  len(self.trajectory))
        t[1].start()
        self._compute()
        t[1].stop()

        _log.info('output file %s', self._output_file)
        _log.info('done %s for %s in %.1f sec [setup:%.0f%%, compute: %.0f%%]',
                  self.long_name,
                  self.tag_description, t[0].wall_time + t[1].wall_time,
                  t[0].wall_time / (t[0].wall_time + t[1].wall_time) * 100,
                  t[1].wall_time / (t[0].wall_time + t[1].wall_time) * 100)
        _log.info('')

        # TODO: refactor
        # Clear data to cut down object memory footprint
        self._pos = []
        self._vel = []
        self._ids = []
        self._pos_unf = []

        # Lists for two-body correlations
        self._pos_0, self._pos_1 = [], []
        self._vel_0, self._vel_1 = [], []
        self._ids_0, self._ids_1 = [], []
        self._pos_unf_0, self._pos_unf_1 = [], []

        return self.grid, self.values

    def __getstate__(self):
        # Unset the trajectory instance and dumps so that the Correlation
        # can be pickled without storing it
        ignore = ['trajectory']
        data = {key: value for key, value in self.__dict__.items() if key not in ignore}
        data = {'grid': self.grid, 'values': self.values, 'analysis': self.analysis}
        return data

    def __setstate__(self, data):
        for key in data:
            setattr(self, key, data[key])

    def _compute(self):
        """Subclasses must implement this"""
        pass

    def analyze(self):
        """
        Subclasses may implement this and store the results in the
        self.analysis dictonary
        """
        pass

    @staticmethod
    def _split_math_func(name):
        if '(' in name:
            name, variables = name.split('(')
            name = name.strip()
            variables = variables.strip().rstrip(')').split(',')
            return name, variables
        return name, None

    @property
    def grid_name(self):
        return self._split_math_func(self.short_name)[1]

    @property
    def _base_name(self):
        return self._split_math_func(self.short_name)[0]

    def _interpolate_path(self, path):
        import re
        # Keep backward compatibility
        path = re.sub('trajectory.filename', 'trajectory', path)
        path = path.format(symbol=self.symbol,
                           qualified_name=self.qualified_name,
                           short_name=self.short_name,
                           long_name=self.long_name.replace(' ', '_'),
                           tag=self.tag,
                           tag_description=self.tag_description.replace(' ', '_'),
                           trajectory=self._trajectory_path)

        # Strip unpleasant punctuation from basename path
        for punct in ['.', '_', '-']:
            subpaths = path.split('/')
            subpaths[-1] = subpaths[-1].replace(punct * 2, punct)
            subpaths[-1] = subpaths[-1].strip(punct)
            path = '/'.join(subpaths)
        return path

    @property
    def _output_file(self):
        """Returns path of output file"""
        # Interpolate the output path string
        if self.output_path is None:
            return None
        else:
            return self._interpolate_path(self.output_path)

    def write(self):
        """
        Write the correlation function and the analysis data to file
        """
        from .helpers import _itemize

        # Exit right away when no output paths are defined
        if self._output_file is None:
            return

        # Pack grid and value into arrays to dump
        if _is_iterable(self.grid[0]) and len(self.grid) == 2:
            x = numpy.array(self.grid[0]).repeat(len(self.values[0]))
            y = numpy.array(self.grid[1] * len(self.grid[0]))
            z = numpy.array(self.values).flatten()
            dump = numpy.transpose(numpy.array([x, y, z]))
        else:
            dump = numpy.transpose(numpy.array([self.grid, self.values]))

        # Comment line
        columns = self.grid_name + [self.qualified_name]
        conj = 'of' if len(self.tag_description) > 0 else ''
        metadata = {
            'title': f'{self.long_name}, {self.qualified_name}, {conj} {self.tag_description}',
            'columns': ', '.join(columns),
        }
        # Add results of analysis in the header
        metadata.update(self.analysis)

        # Write as columnar file
        mkdir(os.path.dirname(self._output_file))
        with open(self._output_file, 'w') as fh:
            for key, value in metadata.items():
                fh.write(f'# {key}: {value}\n')
            numpy.savetxt(fh, dump, fmt="%g")

        # Write analysis as yaml
        # if len(self.analysis) > 0:
        #    import yaml
        #    with open(path + '.yaml', 'w') as fh:
        #        yaml.dump(_itemize(self.analysis), fh)

    def do(self):
        """
        Do the full template pattern: compute, analyze and write the
        correlation function.
        """
        self.compute()
        try:
            self.analyze()
        except ImportError as e:
            _log.warn('Could not analyze due to missing modules, continuing...')
            _log.warn(e)
        self.write()
        return {**self.results, **self.analysis}

    def __call__(self):
        self.do()

    # TODO: deprecate or alias to plot
    def show(self, now=True):
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            return

        if not _is_iterable(self.grid[0]):
            plt.plot(self.grid, self.values, label=self.tag)
            plt.ylabel(self.short_name)
            plt.xlabel(self.grid_name[0])
        if now:
            plt.show()

    def plot(self, show=False, ax=None, fig=None):
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            return

        if not _is_iterable(self.grid[0]):
            if ax is None:
                fig, ax = plt.subplots()
            ax.plot(self.grid, self.values, label=self.tag)
            ax.set_ylabel(self.qualified_name)
            ax.set_xlabel(self.grid_name[0])
        if show:
            fig.show()
        return fig, ax

    def _qualify_name(self, name):
        basename, gridname = self._split_math_func(name)
        tag = '{' + self.tag + '}' if len(self.tag) > 1 else self.tag
        tag = '_' + tag if len(tag) > 0 else ''
        if gridname is not None:
            return basename + tag + '(' + ','.join(gridname) + ')'
        return basename.strip() + tag

    @property
    def qualified_name(self):
        return self._qualify_name(self.short_name)

    def asarray(self):
        assert len(self.grid_name) in [1, 2], f'Unsupported grid dimension={len(self.grid_name)}'

        if len(self.grid_name) == 1:
            return numpy.array([self.grid, self.values])

        if len(self.grid_name) == 2:
            x = numpy.array(self.grid[0]).repeat(len(self.values[0]))
            y = numpy.array(self.grid[1] * len(self.grid[0]))
            z = numpy.array(self.values).flatten()
            return numpy.array([x, y, z])

    @property
    def results(self):
        return {self.qualified_name: self.asarray()}

    @property
    def analysis(self):
        return {self._qualify_name(name.split(',')[1]): value for name, value in self._analysis.items()}

    @analysis.setter
    def analysis(self, value):
        self._analysis = value
