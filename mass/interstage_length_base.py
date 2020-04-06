# -*- coding: utf-8 -*-
"""
  interstage_length_base.py generated by WhatsOpt 1.6.1
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 80

import numpy as np
from openmdao.api import ExplicitComponent

class InterstageLengthBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate InterstageLength discipline """

    def setup(self):
        self.add_input('L_conv', val=1.0, desc='Convergent nozzle section length')
        self.add_input('L_div', val=1.0, desc='Divergent nozzle section length')

        self.add_output('L_interstage', val=np.ones((1,)), desc='Interstage length')



        