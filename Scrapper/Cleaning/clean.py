import numpy as np
import pandas as pd


df1=pd.read_csv("recipe_details.csv")
df2=pd.read_csv("recipe2_details.csv")
df3=pd.read_csv("recipe3_details.csv")
df4=pd.read_csv("recipe4_details.csv")
df5=pd.read_csv("recipe5_details.csv")
df6=pd.read_csv("recipe6_details.csv")
df7=pd.read_csv("recipe7_details.csv")
df8=pd.read_csv("recipe8_details.csv")
df9=pd.read_csv("recipe9_details.csv")
df10=pd.read_csv("recipe10_details.csv")
df11=pd.read_csv("recipe11_details.csv")
df12=pd.read_csv("recipe12_details.csv")
df13=pd.read_csv("recipe13_details.csv")
df14=pd.read_csv("recipe14_details.csv")
df15=pd.read_csv("recipe11.1_details.csv")
df16=pd.read_csv("recipe7.1_details.csv")
df17=pd.read_csv("recipe8.1_details.csv")

data=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14])
pd.set_option('display.max_columns',4)
print(data.info())
print(data.describe())
data=data.dropna()
data=data.drop_duplicates(subset=['url'])
print(data.describe())
print(data.to_csv('final_details.csv',index=False))



