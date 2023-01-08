# microDSC_error_prediction
ML model based on the Decision Tree Regressor algorithm to predict an error (deviation) in the isobaric heat capacity measurement (at 298~K) by microDSC that may arise due to an inappropriate amount of the sample or/and calibration standard material

>The error prediction accuracy of the ML model over the test data is '97.84 %'

# Direction
Use python file 'error_pred_example.py' file to predict the error in heat capacity measurement

**OR**

Minimum Working Example

```python:
  # import module
from modul import *

# prediction of error/deviation in the heat capacity measurement
# use: prediction = dsc_error_model(Reference amount(ml), Sample amount(ml))
# NOTE: enter the sample and reference material amount in [ml] 

# Example 1: Reference amount(ml) = 0.8, Sample amount(ml)= 0.8
# 0.8~ml [full], 0.4~ml [half full], 2.6~ml [one third full]
Reference_amount = 0.8
Sample_amount = 0.8

error_pred = dsc_error_model(Reference_amount,Sample_amount)

```

**OUTPUT**

The example output
```
----------------------------------------------------------------------
Reference volume [mg]:  0.8
Sample volume [mg]:  0.8
Heat capacity measurement deviation prediction (%):  [0.05]
COMMENT(s):
            Sample and reference amount combination is appropriate.
            Consider 0.8~ml as standard amount to avoid any deviation in the measurement.
----------------------------------------------------------------------
```
