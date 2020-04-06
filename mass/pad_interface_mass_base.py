# -*- coding: utf-8 -*-
"""
  pad_interface_mass_base.py generated by WhatsOpt 1.6.1
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 80

import numpy as np
from openmdao.api import ExplicitComponent

class PadInterfaceMassBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate PadInterfaceMass discipline """

    def setup(self):
        self.add_input('Ds', val=1.27, desc='Stage diameter')

        self.add_output('M_pad', val=np.ones((1,)), desc='Pad interface mass')



        