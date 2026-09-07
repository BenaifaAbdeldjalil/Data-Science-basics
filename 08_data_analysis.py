#import pandas modul
import pandas as pd

#read csv file and put it in variable(df)
df = pd.read_csv("dataset/data.csv")

# decsription
print(df.describe())

# decsription
print(df['tax'].describe())

# decsription
print(df['id'].describe())

#mean
print(df.columns)
#print(df["price_paid"].mean()) #TypeError: Cannot perform reduction 'mean' with string dtype
#replace $ with ""
df["price_paid"]=df["price_paid"].apply(lambda x: x.replace("$",""))
#convert type to float
df["price_paid"]=df["price_paid"].astype(float)

print(df["price_paid"].mean()) #6.461930000000001

#sum
print(df["price_paid"].sum()) #6461.93

#min
print(df["price_paid"].min()) #3.0

#max
print(df["price_paid"].max()) #10.0

#unique:
print(df["country"].unique()) #['Canada', 'United States', 'Morocco', 'France', nan]


print(df["country"].unique().tolist())  #['Canada', 'United States', 'Morocco', 'France', nan]


#valuecount
print(df["country"].value_counts()) #agg with  country
print(df["gender"].value_counts()) #agg with  country


#normalize %
print(df["gender"].value_counts(normalize=True).tolist()) #[0.5295381310418904, 0.47046186895810954]

#groupby
print(df.groupby("country").sum()) #all group by country
#print(df.groupby("country").mean()) #all group by country



#groupby
print(df.groupby("gender")["price_paid"].sum()) #all group by country

#groupby list
print(df.groupby(["gender","country"]).sum()) #all group by country
print(df.groupby(["gender","country"])["price_paid"].mean()) #all group by country
print(df.groupby(["gender", "country"])[["price_paid", "tax"]].mean())








