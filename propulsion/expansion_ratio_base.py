# -*- coding: utf-8 -*-
"""
  expansion_ratio_base.py generated by WhatsOpt 1.6.1
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 78

import numpy as np
from openmdao.api import ExplicitComponent

class ExpansionRatioBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate ExpansionRatio discipline """

    def setup(self):
        self.add_input('gamma', val=1.22, desc='Flight path angle')
        self.add_input('gamma_maj', val=np.ones((1,)), desc='Vandenkerckhove function')
        self.add_input('Pc', val= 5610000, desc='')
        self.add_input('Pe', val=18327, desc='')

        self.add_output('epsilon', val=np.ones((1,)), desc='Expansion ratio')



        