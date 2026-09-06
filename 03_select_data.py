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

#data from 10 to 20 lines
print(df[10:20]) #line 20 is not in the list

#with LOC with index numeric
print(df.loc[10:20]) #line 20 is in the list

#with LOC with index varchar
df_email=df.set_index("email")
print(df_email.head(10))
print(df_email.loc['hharridge1@gnu.org']) #
print(type(df_email.loc['hharridge1@gnu.org'])) #<class 'pandas.Series'>



