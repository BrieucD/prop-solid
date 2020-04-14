# -*- coding: utf-8 -*-
"""
  prop_mass_flow_rate_base.py generated by WhatsOpt 1.7.1
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 78


import numpy as np
from numpy import nan
from os import path
from importlib import import_module
from yaml import load, FullLoader
from openmdao.api import ExplicitComponent

class PropMassFlowRateBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate PropMassFlowRate discipline """

    def __init__(self, **kwargs):
        super(PropMassFlowRateBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("prop_mass_flow_rate")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('At', val=np.ones((1,)), desc='Throat area')
        self.add_input('gamma_maj', val=np.ones((1,)), desc='Vandenkerckhove function')
        self.add_input('Pc', val= 5610000, desc='Combustion chamber pressure')
        self.add_input('R', val=286.689655, desc='Specific gas constant')
        self.add_input('Tc', val=1.0, desc='Combustion chamber temperature')

        self.add_output('prop_m', val=np.ones((1,)), desc='Propellantmass flow rate')



        