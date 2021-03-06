# -*- coding: utf-8 -*-
"""
  length_convergent_section.py generated by WhatsOpt 1.7.1
"""
import numpy as np
from solid.length_convergent_section_base import LengthConvergentSectionBase

class LengthConvergentSection(LengthConvergentSectionBase):
    """ An OpenMDAO component to encapsulate LengthConvergentSection discipline """
		
    def compute(self, inputs, outputs):
        """ LengthConvergentSection computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            beta = inputs['beta']
            Ds = inputs['Ds']
            Dt = inputs['Dt']

            L_conv = (Ds - Dt) / (2 * np.sin(beta))

            outputs['L_conv'] = L_conv
        return outputs  

# Reminder: inputs of compute()
#   
#       inputs['beta'] -> shape: (1,), type: Float    
#       inputs['Ds'] -> shape: (1,), type: Float    
#       inputs['Dt'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(LengthConvergentSection, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for LengthConvergentSection """
#   
#       	partials['L_conv', 'beta'] = np.zeros((1, 1))
#       	partials['L_conv', 'Ds'] = np.zeros((1, 1))
#       	partials['L_conv', 'Dt'] = np.zeros((1, 1))        
