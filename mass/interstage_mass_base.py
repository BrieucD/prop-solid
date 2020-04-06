# -*- coding: utf-8 -*-
"""
  interstage_mass_base.py generated by WhatsOpt 1.6.1
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 80

import numpy as np
from openmdao.api import ExplicitComponent

class InterstageMassBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate InterstageMass discipline """

    def setup(self):
        self.add_input('Ds', val=1.27, desc='Stage diameter')
        self.add_input('k_sm', val=1, desc='Interstagematerial correction factor')
        self.add_input('S_int', val=1.0, desc='Interstage surface area')

        self.add_output('M_interstage', val=np.ones((1,)), desc='Interstage mass')



        