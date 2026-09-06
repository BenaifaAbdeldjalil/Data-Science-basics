#import pandas modul
import pandas as pd

#read csv file and put it in variable(df)
df = pd.read_csv("dataset/data.csv")


#nul values
#print(df.isnull())

#notnul values
#print(df.notnull())

#one column
filter = df['tax'].notnull()
#df_nan= df[df['tax'].notnull()]
#print(df_nan)


#replace null values
#df["tax"]= df["tax"].fillna(0)
#print(df)


#replace null values
#df["tax"]= df["tax"].bfill()
# df.fillna(method="ffill")   # ❌ TypeError dans pandas récent
#df.fillna(method="bfill")   # ❌
print(df)


#remouve null values
df_nan= df.dropna(subset=["tax"]) 
print(df_nan) #[654 rows x 10 columns]


df_nann= df.dropna(subset=["tax","country"]) 
print(df_nann) #[628 rows x 10 columns]













