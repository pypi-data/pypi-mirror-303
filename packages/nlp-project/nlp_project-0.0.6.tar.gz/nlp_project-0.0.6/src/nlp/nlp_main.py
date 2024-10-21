#!/usr/bin/env python3
from sklearn.feature_extraction.text import CountVectorizer
import dataclasses
import joblib
import fire

from pkg_resources import resource_filename

class NLPmodel:
  model_path: str = 'nlpmodel.pkl'
  vectorizer_path: str = 'nlpvectorizer.pkl'

  def loadnlpmodel(self):
    try:
      # Use the `files` API to locate and open the binary file
      model_path = resource_filename(__name__, f'{self.model_path}')
      with open(f"{model_path}", "rb") as model:
        return joblib.load(model)
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

  def loadvectorizer(self):
    try:
      # Use the `files` API to locate and open the binary file
      encoder_path = resource_filename(__name__, f'{self.vectorizer_path}')
      with open(f"{encoder_path}", "rb") as vectorizer:
        return joblib.load(vectorizer)
    except Exception as e:
        print(f"Error loading label encoder: {e}")
        return None

vectorizer = NLPmodel().loadvectorizer()
model = NLPmodel().loadnlpmodel()


def nlp_signal(inputs: list):
  doc = ' '.join(inputs)
  #print(doc)
  vector = vectorizer.transform([doc])
  return model.predict(vector)[0]


if __name__ == '__main__':
  fire.Fire(nlp_signal)

