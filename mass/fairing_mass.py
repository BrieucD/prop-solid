# -*- coding: utf-8 -*-
"""
  fairing_mass.py generated by WhatsOpt 1.6.1
"""
import numpy as np
from mass.fairing_mass_base import FairingMassBase

class FairingMass(FairingMassBase):
    """ An OpenMDAO component to encapsulate FairingMass discipline """
		
    def compute(self, inputs, outputs):
        """ FairingMass computation """
    
        outputs['M_fairing'] = np.ones((1,))   

# Reminder: inputs of compute()
#   
#       inputs['Ds'] -> shape: (1,), type: Float    
#       inputs['L_fairing'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(FairingMass, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for FairingMass """
#   
#       	partials['M_fairing', 'Ds'] = np.zeros((1, 1))
#       	partials['M_fairing', 'L_fairing'] = np.zeros((1, 1))        