#import pandas modul
import pandas as pd

#read csv file and put it in variable(df)
df = pd.read_csv("dataset/data.csv")

#haed 5 firts lines
#print(df.head())

#tail 5 latest lines
#print(df.tail())

#haed with more details ex: 8 firts lines
#print(df.head(8))

#shape of dataset
print(df.shape) # (1000, 10)

#columns
#print(df.columns) #Index(['id', 'date', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'country', 'price_paid', 'tax'], dtype='str')

#columns on liste
print(df.columns.tolist()) #['id', 'date', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'country', 'price_paid', 'tax']


#index
print(df.index) #RangeIndex(start=0, stop=1000, step=1)


#modify index, inplace = True modify the original dataframe
df.set_index('id', inplace=True)
#print(df)


print(df.index)









