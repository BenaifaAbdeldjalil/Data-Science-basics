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
print(df_mal) #[438 rows x 10 columns]