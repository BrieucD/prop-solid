# -*- coding: utf-8 -*-
"""
  prop_mass_flow_rate_base.py generated by WhatsOpt 1.6.1
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 78

import numpy as np
from openmdao.api import ExplicitComponent

class PropMassFlowRateBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate PropMassFlowRate discipline """

    def setup(self):
        self.add_input('At', val=np.ones((1,)), desc='Throat area')
        self.add_input('gamma_maj', val=np.ones((1,)), desc='Vandenkerckhove function')
        self.add_input('Pc', val= 5610000, desc='Combustion chamber pressure')
        self.add_input('R', val=286.689655, desc='Specific gas constant')
        self.add_input('Tc', val=75.3, desc='Combustion chamber temperature')

        self.add_output('prop_m', val=np.ones((1,)), desc='Propellantmass flow rate')



        