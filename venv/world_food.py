from pickle import FALSE
import pandas as pd

df1 = pd.read_csv('FAOSTAT_data_7-10-2022 (1).csv', encoding='ISO-8859-1', low_memory =  FALSE)
usefull_columns = [3, 7, 9, 10,11,]
df1=df1[df1.columns[usefull_columns]]

df2= pd.read_csv('FAOSTAT_data_7-10-2022 (3).csv', encoding='ISO-8859-1', low_memory =  FALSE)
df2 = df2[df2.columns[usefull_columns]]
print (df2.head)
