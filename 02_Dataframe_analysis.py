#import pandas modul
import pandas as pd

#read csv file and put it in variable(df)
df = pd.read_csv("dataset/data.csv")

#haed 5 firts lines
#print(df.head())

#tail 5 latest lines
#print(df.tail())

#haed with more details ex: 8 firts lines
print(df.head(8))