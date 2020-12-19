#03-TimeSeriesDecomposition
"
The decomposition of time series is a statistical task that deconstructs a time series into several components
Trend component - which reflects the long-term progression of the series - Trend can be positive or negative or both
Seasonal Component - includes cyclical component
Noise or residual - remainder of the time series after the other components have been removed
AR and MA model assumes time series to be stationary 
and real-world data - they are often governed by a (deterministic) trend and they might have (deterministic) cyclical or seasonal components
"

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



def convert_to_date(x):
  return datetime.strptime(x, '%m/%d/%Y')
  
  

df = pd.read_csv('https://raw/revenue_profit.csv',parse_dates=['Quarter'], date_parser=convert_to_date)


df.head(n=2)
# df.head(n=12)
df.tail(n=2)

print("Rows     :", df.shape[0])
print("Columns  :", df.shape[1])
print("\n Features \n", df.columns.to_list())
print("\n Missing Values \n", df.isnull().any())
print("\n Unique Values \n", df.nunique())


import plotly.express as px
fig = px.line(df, x = 'Quarter',y = 'Revenue',title = 'Amazon Revenue')

fig.update_xaxes(
    rangeslider_visible= True,
    rangeselector=dict(
                        buttons = list([
                        dict(count = 3,label = '1y',step='year',stepmode = "backward"),
                        dict(count = 9,label = '3y',step='year',stepmode = "backward"),
                        dict(count = 15,label = '5y',step='year',stepmode = "backward"),
                        dict(step= 'all')
                            ])        
                        )
                   )
fig.show()


#Null Hypothesis : Data is stationary Alternate Hypothesis : Data is not Stationary
from statsmodels.tsa.stattools import kpss
#Kwiatkowski-Phillips-Schmidt-Shin (kpss)


#Notes:
#The KPSS test will often select fewer differences than the ADF test or a PP test. 
#A KPSS test has a null hypothesis of stationarity, whereas the ADF and PP tests assume that the data have I(1) non-stationarity.

tstest = kpss(df['Revenue'],'ct')
tstest
# 0.17 is the KPSS test stats falls in greater than 2.5% so the Null hypothesis is rejected
#p values is 0.03 which means Null values is rejected
# https://kite.com/python/docs/statsmodels.tsa.stattools.kpss 


#NOTES:
#Interpreting the Results: The KPSS test authors derived one-sided LM statistics for the test. 
#If the LM (The Lagrange Multiplier) statistic is greater than the critical value (given in the table below for alpha levels of 10%, 5% and 1%), 
#then the null hypothesis is rejected; the series is non-stationary.

amazon_df = df.set_index('Quarter')

import statsmodels.api as sm
print("statsmodel has been imported")

res = sm.tsa.seasonal_decompose(amazon_df['Revenue'], model='multiplicative')

res.plot()

plt.figure(figsize=(22,7))
res.trend.plot()

plt.figure(figsize=(22,7))
res.seasonal.plot()


res.observed

print(res.trend)

print(res.seasonal)

print(res.resid)

res.observed[2]
res.seasonal[2]*res.trend[2]*res.resid[2]

#Following plot will give seasonal(Detrended)
pd.DataFrame(res.observed/res.trend).plot()

If it is additive model then
pd.DataFrame(res.observed - res.trend).plot()

































