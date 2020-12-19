
#Importing zip fine in pandas
from download import download
import pandas as pd

path = download('https://archive.ics.uci.edu/ml/machine-learning-databases/00501/PRSA2017_Data_20130301-20170228.zip','/tmp/aq', kind="zip")
df = pd.read_csv('/tmp/aq/PRSA_Data_20130301-20170228/PRSA_Data_Dingling_20130301-20170228.csv', encoding='ISO-8859-1')

#CONVERT DATA from DAY to MONTH or month to year
aq_df_na['TEMP'].resample('1m').mean()

##OFFSET years
aq_df.loc[aq_df_imp.index + pd.offsets.DateOffset(years = -1)]['TEMP']
aq_df_imp = aq_df_imp.reset_index()
aq_df_imp


# Concer int or float to Date format in time series analysis
def convert_to_date(x):
    return datetime.strptime(x, '%Y %m %d %H')

#Combine dates columns
comb_df = pd.read_csv('temp.csv', parse_dates=[['year','month','day','hour']], date_parser=convert_to_date, keep_date_col=True)

# Converting Object date to numeric
df['month'] =  pd.to_numeric(df['month'])
or
df['month'].astype('numeric')
str(df['month']).astype('numeric')


#Best practice to keep mastercopy and working copy (wc)
df_wc = df.copy()

#EDA
df_wc.shpe
df_wc.columns
df_wc.index
df_wc.describe()
df_wc.info()

#GENERAL
print("Rows     :", aq_df.shape[0])
print("Columns  :", aq_df.shape[1])
print("\n Features \n", aq_df.columns.to_list())
print("\n Missing Values \n", aq_df.isnull().any())
print("\n Unique Values \n", aq_df.nunique())


#Missing values check:
aq_df.isnull().values.any()
aq_df.isnull().any()
aq_df.isnull().sum()

#If name not in columns add by using following
df_wc.columns = ['A', 'B','C','D','E','F']

#Date indexing
df_wc = df_wc.set_index('year_month_day_hour')

## 01-TimeSeries_EDA_MIssingValueImputation

#Date indexing
df_wc.index
df_wc.columns

# Extract data from index column using slicing
df_wc.loc['2013-03-01':'2013-03-05']
df_wc.loc['2013':'2015']


#Take the required columns (With and without column names or for multivariate.
df_data = df_wc['PM2.5']
df_data.head(2)

df_data = aq_df.loc[:,['PM2.5']]
df_data.head(2)


#Initial plot
df_data.plot(grid = True)


df_data_2015 = df_data.loc['2015']
df_data_2015 = df_data_2015['PM2.5']
df_data_2015.plot(grid = True)

df_data_2016 = df_data.loc['2016']
df_data_2016 = df_data_2016['PM2.5']
df_data_2016.plot(grid = True)


#PLOTY plotting
import plotly.express as px
fig = px.line(df_data, x = 'year_month_day_hour',y = 'PM2.5',title = 'PM2.5 with slider')

fig.update_xaxes(
    rangeslider_visible= True,
    rangeselector=dict(
                        buttons = list([
                        dict(count = 1,label = '1y',step='year',stepmode = "backward"),
                        dict(count = 2,label = '2y',step='year',stepmode = "backward"),
                        dict(count = 3,label = '3y',step='year',stepmode = "backward"),
                        dict(step= 'all')
                            ])        
                        )
                   )
fig.show()


#PLOTY plotting
fig = px.line(df_data, x = 'year_month_day_hour',y = 'TEMP',title = 'TEMP with slider')

fig.update_xaxes(
    rangeslider_visible= True,
    rangeselector=dict(
                        buttons = list([
                        dict(count = 1,label = '1y',step='year',stepmode = "backward"),
                        dict(count = 2,label = '2y',step='year',stepmode = "backward"),
                        dict(count = 3,label = '3y',step='year',stepmode = "backward"),
                        dict(step= 'all')
                            ])        
                        )
                   )
fig.show()



fig = px.line(df_data, x = 'year_month_day_hour',y = 'TEMP',title = 'TEMP with slider')

fig.update_xaxes(
    rangeslider_visible= True,
    rangeselector=dict(
                        buttons = list([
                        dict(count = 1,label = '1m',step='month',stepmode = "backward"),
                        dict(count = 2,label = '2m',step='month',stepmode = "backward"),
                        dict(count = 3,label = '3m',step='month',stepmode = "backward"),
                        dict(step= 'all')
                            ])        
                        )
                   )
fig.show()


# Comparison year wise data

#Method-1
aq_df['2014':'2015'][['PM2.5','O3']].plot(figsize=(15,8),linewidth= 3,fontsize = 15)
plt.xlabel('year_month_day_hour')

#Method-2
plt.figure(figsize=(16,8))
df_2014 = df_data['2014'].reset_index()
df_2015 = df_data['2015'].reset_index()

df_2014['month_day_hour'] = df_2014.apply(lambda x : str(x['month'])+"."+x['day'],axis = 1)
df_2015['month_day_hour'] = df_2015.apply(lambda x : str(x['month'])+"."+x['day'],axis = 1)

plt.plot(df_2014['month_day_hour'],df_2014['PM2.5'])
plt.plot(df_2015['month_day_hour'],df_2015['PM2.5'])

plt.legend(['2014','2015'])
plt.xlabel('Month')
plt.ylabel('PM2.5')

plt.title('Sale data 2014 and 2015')




# Three years data comparison plot
df_2016 = aq_df['2016'].reset_index()
df_2016['month_day_hour'] = df_2016.apply(lambda x : str(x['month'])+"."+x['day'],axis = 1)

fig = px.line(df_2014, x = 'year_month_day_hour',y='PM2.5',title='PM2.5 with slider')
fig.add_trace(px.line(df_2015,x='year_month_day_hour',y='PM2.5',).data[0])
fig.add_trace(px.line(df_2016,x='year_month_day_hour',y='PM2.5',).data[0])
fig.show()

#Describe
aq_df['2014':'2016'][['month','PM2.5']].groupby('month').describe()

aq_df.groupby('wd').agg(median=('PM2.5','median'),mean=('PM2.5','mean'),max=('PM2.5','max'),min=('PM2.5','min')).reset_index()




#Aggregate function
aq_df['2014':'2016'][['month','PM2.5','TEMP']].groupby('month').agg({'PM2.5':['min','max'],'TEMP':['min','max']})

#Subplots or multiplots (VIMP: There may not be trend only seasonality or cyclicity)

multi_data = aq_df[['PM2.5','TEMP','PRES','RAIN','DEWP']]
multi_data.plot(subplots = True)

aq_df_2015 = aq_df['2015']
pm_data_2015 = aq_df_2015[['PM2.5','TEMP']]
pm_data_2015.plot(subplots = True)


aq_df_2015 = aq_df['2015']
pm_data_2015 = aq_df_2015[['PM2.5','TEMP']]
pm_data_2015.plot()


#PLOTS

#HISTOGRAM (Bimodal or multi model distrinution)
aq_df[['PM2.5','TEMP']].hist()

aq_df[['TEMP']].plot(kind = 'density')

##LAG PLOT (Autoregressive model is a better choice)
# used to check linearity, outliers, randomness, serial correlation or auto correlation, 
#By default lag period is 1 (It is called first order lag plot if lag=1, like that if lag=2 it is called second prder lag plt))
#
pd.plotting.lag_plot(aq_df['TEMP'],lag =1)
#lag plot is a special type of lag scatter plot where x axis is the cuurent time and the y axis is th elag perios
#by default lag period is 1 

#10 hourrly difference
pd.plotting.lag_plot(aq_df['TEMP'],lag =10)

#24 hourrly difference
pd.plotting.lag_plot(aq_df['TEMP'],lag =24)

#1Year difference (+ve correlation)
pd.plotting.lag_plot(aq_df['TEMP'],lag =8640)

#6month difference (-ve correlation)
pd.plotting.lag_plot(aq_df['TEMP'],lag =4320) #negative correlation
#6month difference (NO correlation)
pd.plotting.lag_plot(aq_df['TEMP'],lag =2150) #no correlation


#Pair plot
g = sns.pairplot(aq_df[['PM2.5','SO2','NO2','O3','CO']])


#Correlation plot
aq_corr = aq_df[['PM2.5','SO2','NO2','O3','CO']].corr(method = 'pearson')
aq_corr

sns.heatmap(aq_corr,annot=True)



## AUTO CORRELATION PLOT

aq_df.groupby('wd').agg(median=('PM2.5','median'),mean=('PM2.5','mean'),max=('PM2.5','max'),min=('PM2.5','min')).reset_index()

aq_df_na = aq_df.copy()
aq_df_na = aq_df_na.dropna()  ##NOTE: WE SHOULD NOT DROPT RECORDS IN TIMESERIES ANALYSIS MUST IMPUTE
pd.plotting.autocorrelation_plot(aq_df_na['2014':'2016']['TEMP'])

pd.plotting.autocorrelation_plot(aq_df_na['2014':'2016']['PM2.5'].resample('1m').mean())

pd.plotting.autocorrelation_plot(aq_df_na['2014':'2016']['PM2.5'].resample('1m').mean())


##Handling Missing Value

aq_df[aq_df['PM2.5'].isnull()]
aq_df.isnull().sum()
aq_df.query('TEMP != TEMP')

aq_df.query('TEMP!=TEMP').count()


#ForwardFill
aq_df[aq_df['PM2.5'].isnull()]
aq_df['2015-02-21 10':'2015-02-21 20']
aq_df_imp = aq_df['2015-02-21 10':'2015-02-21 20'][['TEMP']]
aq_df_imp['TEMP_FFILL']= aq_df_imp['TEMP'].fillna(method = 'ffill')#ForwardFill
aq_df_imp


#Backwardfill (SHOULD NOT BE USED)
aq_df_imp['TEMP_BFILL']= aq_df_imp['TEMP'].fillna(method = 'bfill')#Backwardfill

#Rolling mean imputation
aq_df_imp['TEMP_ROLLING'] = aq_df_imp['TEMP'].rolling(window=2, min_periods=1).mean()

#Filling missing value with previos year data imputation
aq_df_imp = aq_df_imp.reset_index()
aq_df_imp['TEMP_PREVY'] = aq_df_imp.apply(lambda x: aq_df.loc[x['year_month_day_hour']- pd.offsets.DateOffset(years = -1)]['TEMP'] if pd.isna(x['TEMP']) else x['TEMP'],axis=1)
aq_df_imp




