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
* This is a Machine learning (ML) model to predict an error due to an inappropriate amount combination of the sample and a reference material in a batch cell of micro-DSC.

* Predict the possible error that may arrise in your experiment with the sample and a reference material amount!

-->ML model uncertainty in prediction is 0.70 (%)<--'''

print(information)
print('-'*70)

class dsc_error_model():
  def __init__(self,Ref,Sam):
    stable_mg = 650 # mg to vol_fraction conversion
    self.Ref = Ref/stable_mg 
    self.Sam = Sam/stable_mg 
    model = joblib.load('dsc_error_dtr.pkl')
    scaler = joblib.load('scaler.pkl')
    data = [Ref, Sam, Ref/Sam]
    data = pd.DataFrame([data])
    data_ = scaler.transform(data)
    pred = model.predict(data_)
    pred_ = ((pred*100)-100).astype(np.float)
    
    print('-'*70)
    print('Reference volume [mg]: ', Ref)
    print('Sample volume [mg]: ', Sam)
    
    if abs(pred_) <= 1.5:
      print('Heat capacity measurement error prediction (%): ', pred_)
      print('''COMMENT(s): 
            Sample and reference mass combination is appropriate.''')
    else:
      print('Heat capacity measurement error prediction (%): ', pred_)
      print('''COMMENT(s): 
            Sample and reference mass is not appropriate.
            The reference material is too low!
            Re-run calibration with the fully filled reference material in a batch cell to avoid a large error.
            ''')
    print('-'*70)
    
    
