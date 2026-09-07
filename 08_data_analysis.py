#import pandas modul
import pandas as pd

#read csv file and put it in variable(df)
df = pd.read_csv("dataset/data.csv")

# replace nan with 0
df["tax"]=df["tax"].fillna(0, inplace=True)


#convert 
df.price_paid=df.price_paid.apply(lambda x: x.replace("$",""))
df.price_paid=df.price_paid.astype(float)

#add column df["tax_price"]
df["tax_price"]=round(df["price_paid"]*(1-df["tax"]/100),2)



#mapping
country={"United State":"USA", 
         "Morocco" :"MAR",
         "Canada":"CNA",
         "France" : "FR"}

df["ind"] = df["country"].map(country)


print(df)

















