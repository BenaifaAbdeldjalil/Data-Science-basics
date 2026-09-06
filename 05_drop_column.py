#import pandas modul
import pandas as pd

#read csv file and put it in variable(df)
df = pd.read_csv("dataset/data.csv")

#Drop axis=1 --> column, axis=0 --> row
#Drop column "ip_adress"
df.drop("ip_address", axis=1, inplace=True)
print(df.columns) #Index(['id', 'date', 'first_name', 'last_name', 'email', 'gender', 'country','price_paid', 'tax'],
#print(df)

#Drop lines "Male"
df.set_index("gender",inplace=True)
df.drop("Male",axis=0,inplace=True)
print(df) #[562 rows x 8 columns]

#drop lot of column
#list= ['id', 'date', 'country','price_paid', 'tax']#
#df.drop(list,axis=1, inplace=True)
##OR

df.drop(['id', 'date', 'country','price_paid', 'tax'],axis=1, inplace=True)
print(df.columns) #Index(['first_name', 'last_name', 'email'], dtype='str')


#other solution

del df['first_name']
print(df.columns) #Index(['last_name', 'email'], dtype='str')

