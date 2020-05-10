# -*- coding: utf-8 -*-
"""
  pad_interface_mass.py generated by WhatsOpt 1.7.1
"""
import numpy as np
from mass.pad_interface_mass_base import PadInterfaceMassBase

class PadInterfaceMass(PadInterfaceMassBase):
    """ An OpenMDAO component to encapsulate PadInterfaceMass discipline """
		
    def compute(self, inputs, outputs):
        """ PadInterfaceMass computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            Ds = inputs['Ds']
            
            M_pad = 25.736 * np.pi * (Ds**2)/4 * (3.2808 * Ds)**0.5498

            outputs['M_pad'] = M_pad
        return outputs    

# Reminder: inputs of compute()
#   
#       inputs['Ds'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(PadInterfaceMass, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for PadInterfaceMass """
#   
#       	partials['M_pad', 'Ds'] = np.zeros((1, 1))        
