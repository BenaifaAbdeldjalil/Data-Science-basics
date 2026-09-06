#import pandas modul
import pandas as pd

#read csv file and put it in variable(df)
df = pd.read_csv("dataset/data.csv")

#filtre gender
#print(df["gender"])

#filtre gender comparaison
#print(df["gender"]=="Male")

#filter the original dataframe with : df["gender"]=="Male"
#df[df["gender"]=="Male"] # df["gender"]=="Male"
#df[df["gender"]=="Male"] #dataframe
#df["gender"]=="Male" #serie just the column
print(df[df["gender"]=="Male"]) #[438 rows x 10 columns]

#"gender"]=="Female"
print(df[df["gender"]=="Female"]) #[493 rows x 10 columns]

#"gender"]not "Female" and not "Male"
print(df[(df["gender"]!="Female") & (df["gender"]!="Male")] ) #[69 rows x 10 columns]

#Tips
male_filter=df["gender"]=="Male"
df_mal=df[male_filter]
#print(df_mal) #[438 rows x 10 columns]

#country
#df_country = df["country"].isin(["France","Canada"])
filter_country=df["country"].isin(["France","Canada"])
print(df[filter_country]) #[569 rows x 10 columns]

#price
#filtre_price= df["price_paid"]>5
#print(df[filtre_price]) #TypeError: '>' not supported between instances of 'str' and 'int'

#solution

#copy data
dftest=df.copy()
#datacleaning
dftest.price_paid=dftest.price_paid.apply(lambda x: x.replace("$",""))

#dataconversion
dftest.price_paid=dftest.price_paid.astype(float)

#filter
filtre_price= dftest["price_paid"]>5
print(dftest[filtre_price]) #[694 rows x 10 columns]



