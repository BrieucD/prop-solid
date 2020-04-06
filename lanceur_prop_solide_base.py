# -*- coding: utf-8 -*-
"""
  lanceur_prop_solide_base.py generated by WhatsOpt 1.6.1
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 77

import numpy as np
from packaging import version

from openmdao.api import Problem, Group, ParallelGroup, IndepVarComp
from openmdao.api import NonlinearBlockGS
from openmdao.api import ScipyKrylov
from openmdao import __version__ as OPENMDAO_VERSION

from propulsion.propulsion import Propulsion
from solid.solid import Solid
from mass.mass import Mass
from propulsion.fonction_vandenkerckhove import FonctionVandenkerckhove
from propulsion.expansion_ratio import ExpansionRatio
from propulsion.throat_area import ThroatArea
from propulsion.prop_mass_flow_rate import PropMassFlowRate
from propulsion.characteristic_velocity import CharacteristicVelocity
from propulsion.thrust_coefficient import ThrustCoefficient
from propulsion.exhaust_velocity import ExhaustVelocity
from propulsion.thrust_force import ThrustForce
from propulsion.specific_impulse import SpecificImpulse
from solid.propellants_mass import PropellantsMass
from solid.solid_rocket_mass import SolidRocketMass
from solid.solid_motor_length import SolidMotorLength
from solid.length_convergent_section import LengthConvergentSection
from solid.length_divergent_section import LengthDivergentSection
from solid.solid_rocket_length import SolidRocketLength
from mass.interstage_length import InterstageLength
from mass.fairing_length import FairingLength
from mass.fairing_mass import FairingMass
from mass.interstage_mass import InterstageMass
from mass.pad_interface_mass import PadInterfaceMass
from mass.avionics_mass import AvionicsMass
from mass.power_subsystem_mass import PowerSubsystemMass
from mass.payload_adapter_mass import PayloadAdapterMass


class LanceurPropSolideBase(Group):
    """ An OpenMDAO base component to encapsulate LanceurPropSolide MDA """
    def __init__(self, thrift_client=None, **kwargs):
        super(LanceurPropSolideBase, self). __init__(**kwargs)

        self.nonlinear_solver = NonlinearBlockGS()       
        self.nonlinear_solver.options['atol'] = 1.0e-10
        self.nonlinear_solver.options['rtol'] = 1.0e-10
        if version.parse(OPENMDAO_VERSION) > version.parse("2.8.0"):
            self.nonlinear_solver.options['err_on_non_converge'] = True
            if version.parse(OPENMDAO_VERSION) > version.parse("2.9.1"):
                self.nonlinear_solver.options['reraise_child_analysiserror'] = False 
        else:
            self.nonlinear_solver.options['err_on_maxiter'] = True
        self.nonlinear_solver.options['iprint'] = 1

        self.linear_solver = ScipyKrylov()       
        self.linear_solver.options['atol'] = 1.0e-10
        self.linear_solver.options['rtol'] = 1.0e-10
        if version.parse(OPENMDAO_VERSION) > version.parse("2.8.0"):
            self.linear_solver.options['err_on_non_converge'] = True
        else:
            self.linear_solver.options['err_on_maxiter'] = True        
        self.linear_solver.options['iprint'] = 1

    def setup(self): 
        indeps = self.add_subsystem('indeps', IndepVarComp(), promotes=['*'])

        indeps.add_output('Ae', 1.5926)
        indeps.add_output('beta', 1.0)
        indeps.add_output('De', 1.424)
        indeps.add_output('Ds', 1.27)
        indeps.add_output('Dt', 1.0)
        indeps.add_output('FF', 0.95)
        indeps.add_output('g0', 9.80665)
        indeps.add_output('gamma', 1.22)
        indeps.add_output('k_sm', 1)
        indeps.add_output('L_vehicle', 1.0)
        indeps.add_output('M_case', 1.0)
        indeps.add_output('M_igniter', 1.0)
        indeps.add_output('M_nozzle', 1.0)
        indeps.add_output('M_PL', 140)
        indeps.add_output('Pa', 26442)
        indeps.add_output('Pc',  5610000)
        indeps.add_output('Pe', 18327)
        indeps.add_output('R', 286.689655)
        indeps.add_output('rho_p', 1.0)
        indeps.add_output('Ru', 1.0)
        indeps.add_output('SF', 0.03)
        indeps.add_output('S_int', 1.0)
        indeps.add_output('tb', 1.0)
        indeps.add_output('Tc', 75.3)
        indeps.add_output('theta_n', 1.0)
        indeps.add_output('zeta', 0.93630)
        self.add_subsystem('Propulsion', self.create_propulsion(), promotes=['Ae', 'Ae', 'Ae', 'At', 'At', 'At', 'C_F', 'C_F', 'C_F', 'C_star', 'C_star', 'C_star', 'epsilon', 'epsilon', 'epsilon', 'F_T', 'F_T', 'g0', 'g0', 'gamma', 'gamma', 'gamma', 'gamma', 'gamma_maj', 'gamma_maj', 'gamma_maj', 'gamma_maj', 'gamma_maj', 'gamma_maj', 'Isp', 'Isp', 'Pa', 'Pa', 'Pc', 'Pc', 'Pc', 'Pc', 'Pe', 'Pe', 'Pe', 'Pe', 'prop_m', 'prop_m', 'prop_m', 'R', 'R', 'R', 'Tc', 'Tc', 'Tc', 'Ve', 'Ve', 'Ve', 'Ve', 'zeta', 'zeta'])
        self.add_subsystem('Solid', self.create_solid(), promotes=['beta', 'beta', 'De', 'De', 'Ds', 'Ds', 'Ds', 'Dt', 'Dt', 'Dt', 'FF', 'FF', 'L_case', 'L_case', 'L_case', 'L_conv', 'L_conv', 'L_conv', 'L_div', 'L_div', 'L_div', 'L_SRM', 'L_SRM', 'Mp', 'Mp', 'Mp', 'Mp', 'M_case', 'M_case', 'M_igniter', 'M_igniter', 'M_nozzle', 'M_nozzle', 'M_SRM', 'M_SRM', 'prop_m', 'prop_m', 'rho_p', 'rho_p', 'Ru', 'Ru', 'SF', 'SF', 'tb', 'tb', 'theta_n', 'theta_n'])
        self.add_subsystem('Mass', self.create_mass(), promotes=['Ds', 'Ds', 'Ds', 'Ds', 'Ds', 'Ds', 'k_sm', 'k_sm', 'L_conv', 'L_conv', 'L_div', 'L_div', 'L_fairing', 'L_fairing', 'L_fairing', 'L_interstage', 'L_interstage', 'L_vehicle', 'L_vehicle', 'M_avionics', 'M_avionics', 'M_avionics', 'M_EPS', 'M_EPS', 'M_fairing', 'M_fairing', 'M_interstage', 'M_interstage', 'M_pad', 'M_pad', 'M_PL', 'M_PL', 'M_PLA', 'M_PLA', 'S_int', 'S_int'])

    def create_propulsion(self):
    	return Propulsion()


    def create_solid(self):
    	return Solid()


    def create_mass(self):
    	return Mass()




# Used by Thrift server to serve disciplines
class LanceurPropSolideFactoryBase(object):
    @staticmethod
    def create_propulsion_fonction_vandenkerckhove():
    	return FonctionVandenkerckhove()
    @staticmethod
    def create_propulsion_expansion_ratio():
    	return ExpansionRatio()
    @staticmethod
    def create_propulsion_throat_area():
    	return ThroatArea()
    @staticmethod
    def create_propulsion_prop_mass_flow_rate():
    	return PropMassFlowRate()
    @staticmethod
    def create_propulsion_characteristic_velocity():
    	return CharacteristicVelocity()
    @staticmethod
    def create_propulsion_thrust_coefficient():
    	return ThrustCoefficient()
    @staticmethod
    def create_propulsion_exhaust_velocity():
    	return ExhaustVelocity()
    @staticmethod
    def create_propulsion_thrust_force():
    	return ThrustForce()
    @staticmethod
    def create_propulsion_specific_impulse():
    	return SpecificImpulse()
    @staticmethod
    def create_solid_propellants_mass():
    	return PropellantsMass()
    @staticmethod
    def create_solid_solid_rocket_mass():
    	return SolidRocketMass()
    @staticmethod
    def create_solid_solid_motor_length():
    	return SolidMotorLength()
    @staticmethod
    def create_solid_length_convergent_section():
    	return LengthConvergentSection()
    @staticmethod
    def create_solid_length_divergent_section():
    	return LengthDivergentSection()
    @staticmethod
    def create_solid_solid_rocket_length():
    	return SolidRocketLength()
    @staticmethod
    def create_mass_interstage_length():
    	return InterstageLength()
    @staticmethod
    def create_mass_fairing_length():
    	return FairingLength()
    @staticmethod
    def create_mass_fairing_mass():
    	return FairingMass()
    @staticmethod
    def create_mass_interstage_mass():
    	return InterstageMass()
    @staticmethod
    def create_mass_pad_interface_mass():
    	return PadInterfaceMass()
    @staticmethod
    def create_mass_avionics_mass():
    	return AvionicsMass()
    @staticmethod
    def create_mass_power_subsystem_mass():
    	return PowerSubsystemMass()
    @staticmethod
    def create_mass_payload_adapter_mass():
    	return PayloadAdapterMass()