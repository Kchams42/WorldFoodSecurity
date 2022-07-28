import numpy as np
import pandas as pd
from io import StringIO
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
 
#Requirement #1- Loading data from 2 CSV files.  Here I am loading 3 seperate csv files, and assigning each their own data frame. 
obese_df = pd.read_csv('FAOSTAT_data_7-18-2022.csv', encoding='ISO-8859-1', low_memory =  False)

undernourished_df= pd.read_csv('FAOSTAT_data_7-18-2022 (2).csv', encoding='ISO-8859-1', low_memory =  False)

gross_production_df = pd.read_csv('FAOSTAT_data_7-18-2022 (1).csv',encoding='ISO-8859-1', low_memory =  False)

#The data sets them selves are very large and one of the biggest issues is there a lot of columns that do not provided usefull 
#information for this project.  Because of this I needed to pull the usefull columns from each data frame. Also due to the nature of the
#data frames I only needed to pull the Country and year columns from one data frame.
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


#Requirement #2- Combine the two data sets. 
#First I combined the Gross Production data frame and the Obese data frame.  I chose these two as the Gross production data frame had the lowest amount of data 
# and would be the limiting factor to the overall combined dataset.  Once combined the obese data set had the necxt lowest missing data.  
combined_frames = [gross_production_df, obese_df]
result_data = pd.concat(combined_frames, axis = 1)
result_data.dropna(subset=['Country'], inplace=True)

#To fill in the missing data we need to "fix" some of the curtrent data we have. As a work around I have popped out the Country Column

country = result_data.pop('Country')

# the Obeses adult columns contained values that the Train Tes SPlitr from Sklearn could not identify, names >.01.  Due to this I masked this data to the value of 0
# I also needed to use the Label Encoder to fix any remaining issues
le=preprocessing.LabelEncoder()
result_data['Obese Adults 18 and Over(millions)'] = pd.to_numeric(result_data['Obese Adults 18 and Over(millions)'], errors= 'coerce')
result_data['Obese Adults 18 and Over(millions)'].mask(result_data['Obese Adults 18 and Over(millions)'] >1 , 0)
result_data['Obese Adults 18 and Over(millions)'] = le.fit_transform(result_data['Obese Adults 18 and Over(millions)'])

#For this project I used the Train Test Split model to fill in my missing data.Below is where I set up this process
x=result_data

#The obese column is where we want to fill in our data
y=result_data['Obese Adults 18 and Over(millions)']
X_train, X_test, y_train, y_test =train_test_split(x,y,test_size=.08 )
lr = LogisticRegression(max_iter=3000)
lr.fit(X_train,y_train)
pred=lr.predict(X_test)

#The metrics below will show up the confidence in our regression results
print(metrics.accuracy_score(pred, y_test))

#Now we I need to add in the final dataframe, the Undernourished dataframe frome above
final_combined = [result_data, undernourished_df]
final_data = pd.concat(final_combined, axis =1)

#Since the dataframes are different sizes I added the country column back then dropped any NaN columns, before popping it out again for the final regression
final_data.insert(0, 'Country', country)
final_data.dropna(subset=['Country'], inplace= True)
country = final_data.pop('Country')
final_data['Undernourished People (millions)'] = pd.to_numeric(final_data['Undernourished People (millions)'], errors= 'coerce')
final_data['Undernourished People (millions)'].mask(final_data['Undernourished People (millions)'] >1, 0)
final_data['Undernourished People (millions)'] = le.fit_transform(final_data['Undernourished People (millions)'])

# We will now use our previous data to fill and complete our data set, using the same regression
x=final_data
y=final_data['Undernourished People (millions)']
X_train, X_test, y_train, y_test =train_test_split(x,y,test_size=.08 )
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train,y_train)
pred=lr.predict(X_test)
print(metrics.accuracy_score(pred, y_test))
result_data=result_data.astype(int)
result_data=result_data.round()
#Adding the Country Column back in
final_data.insert(0, 'Country', country)


#Saving the dataframe to a csv file to use with Tableau
final_data.to_csv('world_food.csv')

print(final_data.head)



