import datetime
import pandas as pd
import requests
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['figure.figsize'] = (10,8)
mpl.rcParams['axes.grid'] = False

print("import succesfull")



coindeskURL = 'https://api.coindesk.com/v1/bpi/historical/close.json?'


start = datetime.date(2017, 1 ,1)
end = datetime.date(2020, 7, 2)

url = f'{coindeskURL}start={start:%Y-%m-%d}&end={end:%Y-%m-%d}'

result = requests.get(url)
result.content



data = pd.read_json(result.content).iloc[:-2,:1]
data.index.name = 'date'
data.index = pd.to_datetime(data.index)
#data = data.drop('disclaimer', 1)
data


data.shape

data.plot()

#resample : this function resamples the the data accordingly
## Upsampling or downsampling the data
data.resample('Q').mean() #Q for Qyarter



data.resample('Q').mean().plot()

data.plot()
data.resample('M').mean().plot()


#D for Calender Day B for Business Day W Weekly M Monthly Q Quarterly A Year end H for Hours T for Minutes S for secinds
#This will help to chek for some pattern

data[:5]

data[:5].diff() #making the first value of column 1 NAN, this will be handy while we want to calculate lag

data[:5].diff(2) #leaving the two values as NAN

pd.concat([data['bpi'],data['bpi'].diff(2),data['bpi'].diff(), data['bpi'].diff(100)],axis=1).plot()
plt.legend(["bpi", "bpi_diif_2","bpi_diif_1", "bpi_diif_n"])

data[:5] #t data

data[:5].shift(2) #t-1 data

data[:5].tshift(2) #It shifts the time by two months, practical use case is corona virus time can be shifted and overlayed with the previos year


data[:5]-data[:5].shift(2)

data[:5]-data[:5].shift()

pd.concat([data,data-data.shift(), data.tshift(365)],axis=1).plot()
plt.legend(["bpi", "bpi_shift()", "bpi_tshift(365)"])


data.rolling(window=10).mean().plot()

data.resample('W').mean().rolling(window = 10).mean().plot() #rolling window is used to calculate the averages


data.resample('W').mean().rolling(window = 10).mean().head(10)


data.rolling(window=50).mean().plot() #rolling window function calculates SMA


data.rolling(window=50,win_type='gaussian').sum(std =10).plot() #if we add window type gaussian with std dev of 10 the it is adding somw weights to the data



data.ewm(span=50).mean().plot() #ewm is exponential moving average, the main purpose of ewm we give more weightage to recent values rather than historical values

pd.concat([data,data.rolling(window=50,win_type='gaussian').sum(std =10),data.ewm(span=50).mean()],axis=1).plot()


rolling_window_100=data.rolling(window=100).mean()
ewm_50 =data.ewm(span=50).mean()
pd.concat([data,rolling_window_100,ewm_50],axis=1).plot()
plt.legend(["data", "rolling_window_100", "ewm_50"])


#we need group by because of scenario

For to check weekend sale.
To compare different month sales


data.groupby(data.index.dayofweek).mean().plot()


data.groupby(data.index.dayofweek).mean().plot()


data.groupby(data.index.month).mean().plot()

data.groupby(data.index.days_in_month).mean().plot()

data.groupby(data.index.year).mean().plot()

data[:5]


data[:5].cumsum()

#Percentage (%) change can be treated.
data[:5].pct_change(2) 

#Pretty similar to cumsum(i.e, cumulative sum which gives only sum) but give other options like mean etc
data[:5].expanding().sum()

data[:5].expanding().mean()

data[:5].expanding(2).mean()


























