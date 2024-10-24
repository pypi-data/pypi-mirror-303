# This file is part of atooms
# Copyright 2010-2024, Daniele Coslovich

"""
Fake decorator to compute partial correlation functions.

It uses filters internally.
"""

import logging

from .helpers import filter_species
from . import core

_log = logging.getLogger(__name__)
    

class Partial(object):

    def __init__(self, corr_cls, *args, **kwargs):
        """
        Compute the partial versions, i.e. by species, of the Correlation
        class `corr_cls`.  The args and kwargs are passed to the
        Correlation constructor. The first positional argument is
        a Trajectory instance.
        """
        # Instantiate correlation objects
        # with args passed upon construction
        self.partial = {}
        self.nbodies = corr_cls.nbodies
        self._output_path = core.pp_output_path

        # Find the species automatically.        
        # Maintain backward compatibility: the species could be passed
        # either as first positional argument or as keyword argument. We
        # remove them from the arguments passed to the correlation.
        if 'species' in kwargs:
            self.species = kwargs.pop('species')            
        else:
            try:
                th = args[0]
                self.species = th[0].distinct_species
            except AttributeError:
                # Compatibility
                self.species = args[0]
                args = args[1: ]

        if self.nbodies == 1:
            for i in range(len(self.species)):
                isp = self.species[i]
                self.partial[isp] = corr_cls(*args, **kwargs)
                self.partial[isp].add_filter(filter_species, isp)
                self.partial[isp].tag = str(isp)
                self.partial[isp].tag_description = 'species %s' % isp

        elif self.nbodies == 2:
            for i in range(len(self.species)):
                for j in range(len(self.species)):
                    isp = self.species[i]
                    jsp = self.species[j]
                    self.partial[(isp, jsp)] = corr_cls(*args, **kwargs)
                    self.partial[(isp, jsp)].add_filter(filter_species, isp)
                    # Slight optimization: avoid filtering twice when isp==jsp
                    if isp != jsp:
                        self.partial[(isp, jsp)].add_filter(filter_species, jsp)
                    self.partial[(isp, jsp)].tag = '%s-%s' % (isp, jsp)
                    self.partial[(isp, jsp)].tag_description = 'species pair %s-%s' % (isp, jsp)

    @property
    def output_path(self):
        return self._output_path

    @output_path.setter
    def output_path(self, path):
        self._output_path = path
        for key in self.partial:
            self.partial[key].output_path = path

    def add_weight(self, trajectory=None, field=None, fluctuations=False):
        for key in self.partial:
            self.partial[key].add_weight(trajectory, field, fluctuations)

    # TODO: drop this
    def need_update(self):
        need = False
        for partial in self.partial.values():
            if partial.need_update():
                need = True
                break
        return need

    def compute(self):
        if self.nbodies == 1:
            for i in range(len(self.species)):
                isp = self.species[i]
                self.partial[isp].compute()

        elif self.nbodies == 2:
            for i in range(len(self.species)):
                for j in range(len(self.species)):
                    isp = self.species[i]
                    jsp = self.species[j]
                    if j >= i or not self.partial[(isp, jsp)]._symmetric:
                        self.partial[(isp, jsp)].compute()
                    else:
                        # The isp-jsp has been already calculated
                        self.partial[(isp, jsp)].grid = self.partial[(jsp, isp)].grid
                        self.partial[(isp, jsp)].value = self.partial[(jsp, isp)].value
                        self.partial[(isp, jsp)].analysis = self.partial[(jsp, isp)].analysis

    def write(self):
        for partial in self.partial.values():
            partial.write()

    def do(self):
        self.compute()
        for partial in self.partial.values():
            try:
                partial.analyze()
            except ImportError as e:
                _log.warn('Could not analyze due to missing modules, continuing...')
                _log.warn(e)
            partial.write()
        return {**self.results, **self.analysis}
            
    def __call__(self):
        self.do()

    @property
    def results(self):
        res = {}
        for partial in self.partial.values():
            res.update(partial.results)
        return res

    @property
    def analysis(self):
        res = {}
        for partial in self.partial.values():
            res.update(partial.analysis)
        return res
    
