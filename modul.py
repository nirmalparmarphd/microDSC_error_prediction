import pandas as pd
import numpy as np
import tensorflow as tf
import tensorflow
import matplotlib as plt
import seaborn as sns
import sklearn
import joblib

print('-'*70)
information ='''
* This is a Machine learning (ML) model based on DecisionTreeRegressor to predict an error due to an inappropriate amount combination of the sample and a reference material in a batch cell of micro-DSC.

* Predict the possible error that may arrise in your experiment with the sample and a reference material amount!

-->The ML Model accuracy is 98.35 (%)<--'''

print(information)
print('-'*70)

class dsc_error_model():
  def __init__(self,Ref,Sam):
    stable_ml = 0.8 # ml to vol_fraction conversion
    self.Ref = Ref/stable_ml
    self.Sam = Sam/stable_ml 
    model = joblib.load('dsc_error_dtr.pkl')
    scaler = joblib.load('scaler.pkl')
    data = [self.Ref, self.Sam, self.Ref/self.Sam]
    data = pd.DataFrame([data])
    data_ = scaler.transform(data)
    pred = model.predict(data_)
    pred_ = ((pred*100)-100).astype(np.float64)
    
    print('-'*70)
    print('Reference volume [mg]: ', Ref)
    print('Sample volume [mg]: ', Sam)
    
    if abs(pred_) <= 1.5:
      print('Heat capacity measurement deviation prediction (%): ', pred_)
      print('''COMMENT(s): 
            Sample and reference amount combination is appropriate.
            Consider 0.8~ml as standard amount to avoid any deviation in the measurement.''')
    else:
      print('Heat capacity measurement deviation prediction (%): ', pred_)
      print('''COMMENT(s): 
            Sample and reference amount maybe not appropriate.
            The reference material may too low!
            Re-run calibration with the fully filled reference material in a batch cell to avoid a large deviation.
            Consider 0.8~ml as standard amount to avoid any deviation in the measurement.
            ''')
    print('-'*70)
    