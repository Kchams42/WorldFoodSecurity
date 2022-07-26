from itertools import count
import re
from turtle import left
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder

obese_df = pd.read_csv('FAOSTAT_data_7-18-2022.csv', encoding='ISO-8859-1', low_memory =  False)

undernourished_df= pd.read_csv('FAOSTAT_data_7-18-2022 (2).csv', encoding='ISO-8859-1', low_memory =  False)

gross_production_df = pd.read_csv('FAOSTAT_data_7-18-2022 (1).csv',encoding='ISO-8859-1', low_memory =  False)


obese_usefull_columns = [11]
obese_df = obese_df[obese_df.columns[obese_usefull_columns]]
obese_df.rename(columns = { 'Value' : 'Obese Adults 18 and Over(millions)'}, inplace = True)

undernourished_usefull_columns = [11]
undernourished_df = undernourished_df[undernourished_df.columns[undernourished_usefull_columns]]
undernourished_df.rename (columns = {'Value' : 'Undernourished People (millions)'}, inplace = True)

gross_production_usefull_columns = [3, 9, 11]
gross_production_df = gross_production_df[gross_production_df.columns[gross_production_usefull_columns]]
gross_production_df.rename (columns = {'Value' : 'Total Agricultural Production (millions)',  'Area' : 'Country'}, inplace= True)
gross_production_df=gross_production_df.interpolate()



combined_frames = [gross_production_df, obese_df]
result_data = pd.concat(combined_frames, axis = 1)
result_data.dropna(subset=['Country'], inplace=True)
#print(result_data.head)

le= preprocessing.LabelEncoder()
#le.fit(result_data['Country'])
#print(list(le.classes_))
result_data['Country']= le.fit_transform(result_data['Country'])
#print(result_data.head)
#result_data = result_data
result_data['Obese Adults 18 and Over(millions)'] = pd.to_numeric(result_data['Obese Adults 18 and Over(millions)'], errors= 'coerce')
result_data['Obese Adults 18 and Over(millions)'].mask(result_data['Obese Adults 18 and Over(millions)'] >1 , 0)
result_data['Obese Adults 18 and Over(millions)'] = le.fit_transform(result_data['Obese Adults 18 and Over(millions)'])

x=result_data
y=result_data['Obese Adults 18 and Over(millions)']

X_train, X_test, y_train, y_test =train_test_split(x,y,test_size=.08 )
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train,y_train)
pred=lr.predict(X_test)
print(metrics.accuracy_score(pred, y_test))
print ()
print (result_data.head())
result_data['Country']=le.inverse_transform(result_data['Country'])
result_data =  result_data





final_combined = [result_data, undernourished_df]
final_data = pd.concat(final_combined, axis =1)
final_data.dropna(subset=['Country'], inplace= True)
final_data['Undernourished People (millions)'] = pd.to_numeric(final_data['Undernourished People (millions)'], errors= 'coerce')
final_data['Undernourished People (millions)'].mask(final_data['Undernourished People (millions)'] >1, 0)
final_data['Undernourished People (millions)'] = le.fit_transform(final_data['Undernourished People (millions)'])
x=final_data
print(final_data.isna)
y=final_data['Undernourished People (millions)']
X_train, X_test, y_train, y_test =train_test_split(x,y,test_size=.08 )
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train,y_train)
pred=lr.predict(X_test)
print(metrics.accuracy_score(pred, y_test))
print ()

print (final_data.head())


