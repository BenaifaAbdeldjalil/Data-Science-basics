#import pandas modul
import pandas as pd

#read csv file and put it in variable(df)
df = pd.read_csv("dataset/data.csv")

#haed 5 firts lines
#print(df.head())


#select email column
#print(df["email"].head())

#or 
print(df.email.head())

#dataframe vs serie
#dataframe 
print(type(df)) #<class 'pandas.DataFrame'>

#Serie
print(type(df.email)) #<class 'pandas.Series'>









