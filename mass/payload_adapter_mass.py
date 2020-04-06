# -*- coding: utf-8 -*-
"""
  payload_adapter_mass.py generated by WhatsOpt 1.6.1
"""
import numpy as np
from mass.payload_adapter_mass_base import PayloadAdapterMassBase

class PayloadAdapterMass(PayloadAdapterMassBase):
    """ An OpenMDAO component to encapsulate PayloadAdapterMass discipline """
		
    def compute(self, inputs, outputs):
        """ PayloadAdapterMass computation """
    
        outputs['M_PLA'] = np.ones((1,))   

# Reminder: inputs of compute()
#   
#       inputs['M_PL'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(PayloadAdapterMass, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for PayloadAdapterMass """
#   
#       	partials['M_PLA', 'M_PL'] = np.zeros((1, 1))        
