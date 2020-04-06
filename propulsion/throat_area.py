# -*- coding: utf-8 -*-
"""
  throat_area.py generated by WhatsOpt 1.6.1
"""
import numpy as np
from propulsion.throat_area_base import ThroatAreaBase

class ThroatArea(ThroatAreaBase):
    """ An OpenMDAO component to encapsulate ThroatArea discipline """
		
    def compute(self, inputs, outputs):
        """ ThroatArea computation """
        
        At=Ae/epsilon
    
        outputs['At'] = np.ones((1,))   

# Reminder: inputs of compute()
#   
#       inputs['Ae'] -> shape: (1,), type: Float    
#       inputs['epsilon'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(ThroatArea, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for ThroatArea """
#   
#       	partials['At', 'Ae'] = np.zeros((1, 1))
#       	partials['At', 'epsilon'] = np.zeros((1, 1))        