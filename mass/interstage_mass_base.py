# -*- coding: utf-8 -*-
"""
  interstage_mass_base.py generated by WhatsOpt 1.7.1
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 80


import numpy as np
from numpy import nan
from os import path
from importlib import import_module
from yaml import load, FullLoader
from openmdao.api import ExplicitComponent

class InterstageMassBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate InterstageMass discipline """

    def __init__(self, **kwargs):
        super(InterstageMassBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("interstage_mass")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('Ds', val=1.27, desc='Stage diameter')
        self.add_input('k_sm', val=1, desc='Interstagematerial correction factor')
        self.add_input('S_int', val=1.0, desc='Interstage surface area')

        self.add_output('M_interstage', val=np.ones((1,)), desc='Interstage mass')



        