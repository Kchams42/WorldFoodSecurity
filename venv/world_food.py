from itertools import count
import numpy as np
import pandas as pd
import sklearn

#Loading in both data sets, due to certian data types in the set a differernt encoding needed to be used.
#Also due to the large size of the data set low_memory needed to be set to flase

obese_df = pd.read_csv('FAOSTAT_data_7-18-2022.csv', encoding='ISO-8859-1', low_memory =  False)

undernourished_df= pd.read_csv('FAOSTAT_data_7-18-2022 (2).csv', encoding='ISO-8859-1', low_memory =  False)

gross_production_df = pd.read_csv('FAOSTAT_data_7-18-2022 (1).csv',encoding='ISO-8859-1', low_memory =  False)

#Many columns were not useful to this project, so those columns needed to be removed.  
#Columns also used a fairly generic name(value), and the parameter for each value even though they were the same
#I combined the value column with the descriptor.
obese_usefull_columns = [3,  9, 11,]
obese_df = obese_df[obese_df.columns[obese_usefull_columns]]
obese_df.rename(columns = {'Area' : 'Country', 'Value' : 'Obese Adults 18 and Over(millions)'}, inplace = True)

undernourished_usefull_columns = [11]
undernourished_df = undernourished_df[undernourished_df.columns[undernourished_usefull_columns]]
undernourished_df.rename (columns = {'Value' : 'Undernourished People (millions)'}, inplace = True)

gross_production_usefull_columns = [9,11]
gross_production_df = gross_production_df[gross_production_df.columns[gross_production_usefull_columns]]
gross_production_df.rename (columns = {'Value' : 'Total Agricultural Production (millions)'}, inplace= True)
gross_production_df=gross_production_df.interpolate()
print (gross_production_df.info())

#Joining the 3 datasets together 
combined_frames = [obese_df, undernourished_df, gross_production_df]
result_data = pd.concat(combined_frames, axis = 1)

#rearanging the columns
year_column = result_data.pop('Year',)
result_data.insert(1, 'Year', year_column)
production_column = result_data.pop ('Total Agricultural Production (millions)')
result_data.insert(2, 'Total Agricultural Production (millions)', production_column)


print (result_data.info())

#print (result_data.info())

#step 1 fill/drop total agricultural production in the gross production data frame
#step 2 using total agticultural production data frame use linear regression to fill obese and undernourished data frames
#step 3 concat all 3 data frames
#https://www.analyticsvidhya.com/blog/2021/05/dealing-with-missing-values-in-python-a-complete-guide/
#https://python.plainenglish.io/predict-missing-dataframe-values-with-an-ml-algorithm-717cd872f1a8
#https://www.kaggle.com/code/punit0811/linear-regression-with-titanic-dataset