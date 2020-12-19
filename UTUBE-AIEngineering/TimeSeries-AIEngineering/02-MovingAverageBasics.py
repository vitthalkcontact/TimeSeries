!pip install download


from __future__ import absolute_import,division,print_function,unicode_literals

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

import pandas as pd

from download import download

mpl.rcParams['figure.figsize'] = (8,6)
mpl.rcParams['axes.grid'] = False

print("Import Succesfull")


def parse(x):
  return datetime.strptime(x, '%m/%d/%Y')
  
  
df = pd.read_csv('https://electricity_consumption.csv',  parse_dates=['Bill_Date'], date_parser=parse)



print("Rows     :", df.shape[0])
print("Columns  :", df.shape[1])
print("\n Features \n", df.columns.to_list())
print("\n Missing Values \n", df.isnull().any())
print("\n Unique Values \n", df.nunique())



bill_df = df.set_index('Bill_Date')
bill_df.head(2)



bill_2018 = bill_df['2016':'2018'][['Billed_amount']]

bill_2018

***********************
NOTES:
"
#Simple Moving Average

The Simple Moving Average (SMA) is calculated by adding the price of an instrument 
over a number of time periods and then dividing the sum by the number of time periods. 
The SMA is basically the average price of the given time period, with equal weighting given to the price of each period.
In financial applications a simple moving average (SMA) is the unweighted mean of the previous n data. 
However, in science and engineering, the mean is normally taken from an equal number of data on either side of a central value. 
This ensures that variations in the mean are aligned with the variations in the data rather than being shifted in time.

Mathmatically (t+(t-1)+(t-2)+...+(t-n))/n

Moving Average cant be a great tool when, the data is not stationary and fluctuating.
"
***********************************


bill_2018['Billed_amount'].rolling(window=3).mean()
bill_2018['ma_rolling_3']= bill_2018['Billed_amount'].rolling(window=3).mean().shift(1)
bill_2018
bill_2018.plot()

***********************************
NOTES:
"
#Weighted Moving Average

Weighted moving averages can find trens sooner than SMA (Simple Moving Average), 
on the other hand its complex as we need to assign the weights manually.
"
***********************************



def wma(weights):
  def calc(x):
    return (weights*x).mean()
  return calc
  


#The weights should add up to the window value
bill_2018['wma_rolling_3']= bill_2018['Billed_amount'].rolling(window = 3).apply(wma(np.array([0.5,1,1.5]))).shift(3)
bill_2018
bill_2018.plot()



#Exponential Moving Average

***********************************
NOTES:
It adopts quickly to the data point changes ,and we dont have to decide the weights manually.
***********************************

bill_2018['ewm_window_3']= bill_2018['Billed_amount'].ewm(span = 3,adjust = False,min_periods = 0).mean().shift(1)
bill_2018




#Exponential Smoothing

***********************************
NOTES:

It Requires a parameter called alpha aka Smoothing parameter.
alpha: Smoothing function or smoothing coefficient. Its value ranges between 0 and 1.

Larger value of alpha means the model is paying attention to the newer values,
smaller value of alpha mean model is giving importance to history value.

***********************************


bill_2018['esm_windiw_3_7'] = bill_2018['Billed_amount'].ewm(alpha = 0.7 , adjust = False ,min_periods = 3).mean().shift(1)
bill_2018.plot()


bill_2018['esm_windiw_3_3'] = bill_2018['Billed_amount'].ewm(alpha = 0.3 , adjust = False ,min_periods = 3).mean().shift(1)

bill_2018[['Billed_amount','esm_windiw_3_7','esm_windiw_3_3']].plot()


bill_2018


#Evaluation

((bill_2018['Billed_amount']-bill_2018['ma_rolling_3'])**2).mean()**0.5

((bill_2018['Billed_amount']-bill_2018['wma_rolling_3'])**2).mean()**0.5


((bill_2018['Billed_amount']-bill_2018['ewm_window_3'])**2).mean()**0.5


((bill_2018['Billed_amount']-bill_2018['esm_windiw_3_7'])**2).mean()**0.5


((bill_2018['Billed_amount']-bill_2018['esm_windiw_3_3'])**2).mean()**0.5





















