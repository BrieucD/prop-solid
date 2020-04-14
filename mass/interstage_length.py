# -*- coding: utf-8 -*-
"""
  interstage_length.py generated by WhatsOpt 1.7.1
"""
import numpy as np
from mass.interstage_length_base import InterstageLengthBase

class InterstageLength(InterstageLengthBase):
    """ An OpenMDAO component to encapsulate InterstageLength discipline """
		
    def compute(self, inputs, outputs):
        """ InterstageLength computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            L_conv = inputs['L_conv']
            L_div = inputs['L_div']
            outputs['L_interstage'] = L_interstage
        return outputs  
 

# Reminder: inputs of compute()
#   
#       inputs['L_conv'] -> shape: (1,), type: Float    
#       inputs['L_div'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(InterstageLength, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for InterstageLength """
#   
#       	partials['L_interstage', 'L_conv'] = np.zeros((1, 1))
#       	partials['L_interstage', 'L_div'] = np.zeros((1, 1))        
