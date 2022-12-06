# microDSC_error_prediction
ML model to predict an error in the isobaric heat capacity measurement (at 298~K) by microDSC that may arise due to an inappropriate amount of the sample or/and calibration standard material

>Uncertainty of the ML model in the error prediction is '0.70 %'

# Direction
Use python file 'error_pred_example.py' file to predict the error in heat capacity measurement

*OR*

Minimum Working Example

```python:
  # importing module and error prediction function
  from module import *' 
  
  # defining sample and reference materials mass in [mg]
  Reference_mass = 650 
  Sample_mass = 650
  
  # prediction of error in the isobaric heat capacity measurement in [%]
  error_pred = dsc_error_model(Reference_mass,Sample_mass)

```
