#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 10:59:59 2021

@author: neenu
"""

print("Hello world")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import matplotlib as mpl
from datetime import datetime
import numpy as np
#import pandas_profiling
#profile = dataframe.profile_report()
#profile
dataframe_raw = pd.read_csv("DF_Raw_Data.csv", header=0)
dataframe_stdev = pd.read_csv("DF_Rolling_Stdev.csv", header=0)
print (dataframe_raw.describe())
print (dataframe_raw.info())
dataframe_raw = pd.read_csv("DF_Raw_Data.csv", header=0)
dataframe_stdev = pd.read_csv("DF_Rolling_Stdev.csv", header=0)
print (dataframe_raw.describe())
print (dataframe_raw.info())
dataframe_stdev = pd.read_csv("DF_Rolling_Stdev.csv", header=0)
dataframe_raw = pd.read_csv("DF_Raw_Data.csv", header=0)
dataframe_stdev = pd.read_csv("DF_Rolling_Stdev.csv", header=0)
print (dataframe_raw.describe())
print (dataframe_raw.info())
(dataframe_raw < (Q1 - 1.5 * IQR))|(dataframe_raw > (Q3 + 1.5 * IQR))
dataframe_raw = pd.read_csv("DF_Raw_Data.csv", header = 0)
dataframe_raw = pd.read_csv("DF_Raw_Data.csv", header = 0)
dataframe_raw = pd.read_csv("DF_Raw_Data.csv", header=0)
dataframe_stdev = pd.read_csv("DF_Rolling_Stdev.csv", header=0)
print (dataframe_raw.describe())
print (dataframe_raw.info())
sns.boxplot(data= dataframe_raw, color='none', linewidth='1.0')
mpl.rcParams['figure.figsize'] = (15,5)
plt.show()
(dataframe_raw < (Q1 - 1.5 * IQR))|(dataframe_raw > (Q3 + 1.5 * IQR))
(dataframe_raw < (Q1 - 1.5 * IQR))|(dataframe_raw > (Q3 + 1.5 * IQR))
plt.figure(figsize=(12,12))
corr = dataframe_raw.drop(['Data Source', 'TIMEFRAME (DD/MM/YYYY)'],axis=1).corr()
plt.ylabel("PUMP FAILURE (1 or 0)")
plt.title("Heatmap w/ respect to Failure Mode with Raw features")
sns.heatmap(corr, annot=True, square = True)
plt.figure(figsize=(20,20))
corr = dataframe_stdev.drop(['Data Source', 'TIMEFRAME (DD/MM/YYYY)'],axis=1).corr()
plt.ylabel("PUMP FAILURE (1 or 0)")
plt.title("Correlation matrix using 'raw' variables")
sns.heatmap(corr, annot=True, square = True)



                            
