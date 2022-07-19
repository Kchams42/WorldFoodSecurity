import numpy as np
import pandas as pd
import webbrowser

#Loading in both data sets, due to certian data types in the set a differernt encoding needed to be used.
#Also due to the large size of the data set low_memory needed to be set to flase

obese_df = pd.read_csv('FAOSTAT_data_7-18-2022.csv', encoding='ISO-8859-1', low_memory =  False)

undernourished_df= pd.read_csv('FAOSTAT_data_7-18-2022 (2).csv', encoding='ISO-8859-1', low_memory =  False)

gross_production_df = pd.read_csv('FAOSTAT_data_7-18-2022 (1).csv',encoding='ISO-8859-1', low_memory =  False)

#Many columns were not useful to this project, so those columns needed to be removed.  

obese_usefull_columns = [3, 7, 9, 11,]
obese_df = obese_df[obese_df.columns[obese_usefull_columns]]

concat_usefull_columns = [7, 11]
undernourished_df = undernourished_df[undernourished_df.columns[concat_usefull_columns]]
gross_production_df = gross_production_df[gross_production_df.columns[concat_usefull_columns]]

#Joining the 2 datasets together 
combined_frames = [obese_df, undernourished_df, gross_production_df]
result_data = pd.concat(combined_frames, axis = 1)

#rearanging the columns
year_column = result_data.pop('Year')
result_data.insert(1, 'Year', year_column)
print (result_data.info())

#print (result_data.info())