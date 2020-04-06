# -*- coding: utf-8 -*-
"""
  thrust_force.py generated by WhatsOpt 1.6.1
"""
import numpy as np
from propulsion.thrust_force_base import ThrustForceBase

class ThrustForce(ThrustForceBase):
    """ An OpenMDAO component to encapsulate ThrustForce discipline """
		
    def compute(self, inputs, outputs):
        """ ThrustForce computation """
    
        outputs['F_T'] = np.ones((1,))   

# Reminder: inputs of compute()
#   
#       inputs['Ae'] -> shape: (1,), type: Float    
#       inputs['Pa'] -> shape: (1,), type: Float    
#       inputs['Pe'] -> shape: (1,), type: Float    
#       inputs['prop_m'] -> shape: (1,), type: Float    
#       inputs['Ve'] -> shape: (1,), type: Float    
#       inputs['zeta'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(ThrustForce, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for ThrustForce """
#   
#       	partials['F_T', 'Ae'] = np.zeros((1, 1))
#       	partials['F_T', 'Pa'] = np.zeros((1, 1))
#       	partials['F_T', 'Pe'] = np.zeros((1, 1))
#       	partials['F_T', 'prop_m'] = np.zeros((1, 1))
#       	partials['F_T', 'Ve'] = np.zeros((1, 1))
#       	partials['F_T', 'zeta'] = np.zeros((1, 1))        
