# -*- coding: utf-8 -*-
"""
  avionics_mass_base.py generated by WhatsOpt 1.6.1
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 80

import numpy as np
from openmdao.api import ExplicitComponent

class AvionicsMassBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate AvionicsMass discipline """

    def setup(self):
        self.add_input('Ds', val=1.27, desc='Stage diameter')
        self.add_input('L_vehicle', val=1.0, desc='')

        self.add_output('M_avionics', val=np.ones((1,)), desc='')



        