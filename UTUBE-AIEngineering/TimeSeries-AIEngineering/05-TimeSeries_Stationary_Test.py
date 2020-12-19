#TESTING TIME SERIES IS STATIONARY OR NON-STATIONARY:

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime
import pandas as pd
import plotly.express as px

import warnings
warnings.filterwarnings('ignore')


mpl.rcParams['figure.figsize'] = (10, 8)
mpl.rcParams['axes.grid'] = False



def parse(x):
	return datetime.strptime(x, '%m/%d/%Y')

df = pd.read_csv('https://raw.githubusercontent.com/srivatsan88/YouTubeLI/master/dataset/amazon_revenue_profit.csv', parse_dates = ['Quarter'],date_parser=parse)
df.head()



fig = px.line(df, x='Quarter', y='Revenue', title='Amazon Revenue Slider')
fig.update_xaxes(
    rangeslider_visible=True,
)
fig.show()

##KPSS TEST
#Null hypothesis - Series is stationary
#Alternate hypothesis - Series is not stationary

from statsmodels.tsa.stattools import kpss

stats, p, lags, critical_values = kpss(df['Revenue'], 'ct')


print(f'Test Statistics: {stats}')
print(f'p-value: {p}')
print(f'Critial Values: {critical_values}')

if p < 0.05 :
  print('Series is not Stationary')
else:
  print('Series is Stationary')
  

##adfuller
#Null Hypothesis - Series possesses a unit root and hence is not stationary
#Alternate Hypothesis - Series is stationary

from statsmodels.tsa.stattools import adfuller
result = adfuller(df['Revenue'])


print(f'Test Statistics: {result[0]}')
print(f'p-value: {result[1]}')
print(f'Critial Values: {result[4]}')

if result[1] > 0.05 :
  print('Series is not Stationary')
else:
  print('Series is Stationary')


















































