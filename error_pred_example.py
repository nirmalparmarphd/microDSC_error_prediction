### MINIMUM WORKING EXAMPLE ###

# import module
from modul import *

# prediction of error
# use: prediction = dsc_error_model(Reference mass(mg), Sample mass(mg))
# NOTE: enter the sample and reference material mass in [mg] 

# Example 1: Reference mass(mg) = 650, Sample mass(mg)= 600
Reference_mass = 250
Sample_mass = 140
error_pred = dsc_error_model(Reference_mass,Sample_mass)

