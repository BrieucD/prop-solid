# -*- coding: utf-8 -*-
"""
  solid_motor_length_base.py generated by WhatsOpt 1.6.1
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 79

import numpy as np
from openmdao.api import ExplicitComponent

class SolidMotorLengthBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate SolidMotorLength discipline """

    def setup(self):
        self.add_input('Ds', val=1.27, desc='Stage diameter')
        self.add_input('FF', val=0.95, desc='Fill factor')
        self.add_input('Mp', val=np.ones((1,)), desc='')
        self.add_input('rho_p', val=1.0, desc='Propellant density')

        self.add_output('L_case', val=np.ones((1,)), desc='')



        