# for file system import
from imit_main import imit_signal as imit # for file import
from nlp_main import nlp_signal as nlp # for file import

# for install import
#from nlp.imit_main import imit_signal as imit # for file import
#from nlp.nlp_main import nlp_signal as nlp # for file import

import numpy as np
import pandas as pd
import sys

def getSignal(*args):
    try:
        return imit(*args)
    except Exception as e:
        print(e)


df = pd.read_csv('../jupyter/indicators.csv')
#df = df[df['actions'] == 'go_short'].tail(50)
df.drop(['Unnamed: 0'], inplace=True, axis=1)

df = df[df['enter_reason'] == 'first_buy'].head(50)
df['actions'] = df.apply(lambda row: getSignal(  row['open'], row['high'], row['ema-26'], row['ema-12'], row['low'],
                                                row['mean-grad-hist'], row['close'], row['volume'], row['sma-25'],
                                                row['long_jcrosk'], row['short_kdj']
                                              ), axis=1)


# Convert Series to list
print(df.head())

string_series = pd.Series(df['actions'].tolist())

# Function to create sliding windows
def sliding_windows(series=string_series, window_size=3):
    for i in range(len(series) - window_size + 1):
        yield series[i:i + window_size]

predictions = [np.nan] * len(string_series)  # Start with NaN, predictions will overwrite later

# Create sliding windows and predict
window_size = 3  # Sliding window size of 5
for i, window in enumerate(sliding_windows(series=string_series, window_size=3)):
    pred = nlp(window)  # Replace with your actual model's predict function
    predictions[i + window_size - 1] = pred

df['nlpreds'] = predictions
accuracy = len(df[df['nlpreds'] == df['actions']]) * 100/len(df)
print(f'accuracy: --> {accuracy} %')
df['reward'] = df['profit_abs']
df.loc[:,'is_short'] = np.where(df['enter_reason'] == 'first_buy', 0, 1)

print(df.head(15))
df.to_csv('../jupyter/rlhf.csv')