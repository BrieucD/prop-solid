# -*- coding: utf-8 -*-
"""
  thrust_force_base.py generated by WhatsOpt 1.6.1
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 78

import numpy as np
from openmdao.api import ExplicitComponent

class ThrustForceBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate ThrustForce discipline """

    def setup(self):
        self.add_input('Ae', val=1.5926, desc='Nozzle exit area')
        self.add_input('Pa', val=26442, desc='Ambient pressure')
        self.add_input('Pe', val=18327, desc='Nozzle exit pressure')
        self.add_input('prop_m', val=np.ones((1,)), desc='Propellantmass flow rate')
        self.add_input('Ve', val=np.ones((1,)), desc='Exhaust gas true exhaust velocity')
        self.add_input('zeta', val=0.93630, desc='Thrust correction factor')

        self.add_output('F_T', val=np.ones((1,)), desc='Thrust force')



        