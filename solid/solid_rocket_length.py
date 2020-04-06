# -*- coding: utf-8 -*-
"""
  solid_rocket_length.py generated by WhatsOpt 1.6.1
"""
import numpy as np
from solid.solid_rocket_length_base import SolidRocketLengthBase

class SolidRocketLength(SolidRocketLengthBase):
    """ An OpenMDAO component to encapsulate SolidRocketLength discipline """
		
    def compute(self, inputs, outputs):
        """ SolidRocketLength computation """
    
        outputs['L_SRM'] = np.ones((1,))   

# Reminder: inputs of compute()
#   
#       inputs['L_case'] -> shape: (1,), type: Float    
#       inputs['L_conv'] -> shape: (1,), type: Float    
#       inputs['L_div'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(SolidRocketLength, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for SolidRocketLength """
#   
#       	partials['L_SRM', 'L_case'] = np.zeros((1, 1))
#       	partials['L_SRM', 'L_conv'] = np.zeros((1, 1))
#       	partials['L_SRM', 'L_div'] = np.zeros((1, 1))        
