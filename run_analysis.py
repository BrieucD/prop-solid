# -*- coding: utf-8 -*-
"""
  run_analysis.py generated by WhatsOpt 1.6.1
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 77

from openmdao.api import Problem
from run_parameters_init import initialize
from lanceur_prop_solide import LanceurPropSolide 

pb = Problem(LanceurPropSolide())
pb.setup()  

initialize(pb)

pb.run_model()   
pb.model.list_inputs(print_arrays=False)
pb.model.list_outputs(print_arrays=False)

