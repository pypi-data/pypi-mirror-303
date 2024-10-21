#!/usr/bin/env python3
from sklearn.preprocessing import LabelEncoder
import joblib
import numpy as np
from pkg_resources import resource_filename
#import importlib.resources as resources
import fire, warnings
from dataclasses import dataclass
import pandas as pd

@dataclass
class Regbot:
  opening: float
  high: float
  ema_26: float
  ema_12: float
  low: float
  mean_grad_hist: int
  close: float
  volume: float
  sma_25: float
  long_jcrosk: int
  short_kdj: int


  imit_model_path: str = resource_filename(__name__, 'imit_model.pkl')
  label_encoder_path: str = resource_filename(__name__, 'imit_label_encoder.pkl')

  def loadmodel(self):
    try:
      # Use the `files` API to locate and open the binary file
      model_path = resource_filename(__name__, 'imit_model.pkl')
      with open(f"{model_path}", "rb") as model:
        return joblib.load(model)
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

  def loadencoder(self):
    try:
      # Use the `files` API to locate and open the binary file
      encoder_path = resource_filename(__name__, 'imit_label_encoder.pkl')
      with open(f"{encoder_path}", "rb") as encoder:
        return joblib.load(encoder)
    except Exception as e:
        print(f"Error loading label encoder: {e}")
        return None


  def prepareInput(self):
    stuff = [ self.opening, self.high, self.ema_26,
              self.ema_12, self.low,
              self.mean_grad_hist, self.close,
              self.volume,
              self.sma_25,
              self.long_jcrosk,
              self.short_kdj
          ]
    try:
      return np.array([stuff])
    except Exception as e:
      print(e)


  def buySignalGenerator(self):
    try:
      model = self.loadmodel()
      data = self.prepareInput().reshape(1,-1)
      preds = model.predict(data)
      label_encoder = self.loadencoder()
      return label_encoder.inverse_transform(preds.astype(int))
    except Exception as e:
      print(e)


def imit_signal(*args):
    try:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            return Regbot(*args).buySignalGenerator()[0]
    except Exception as e:
        print(e)


if __name__ == '__main__':
  fire.Fire(imit_signal)

