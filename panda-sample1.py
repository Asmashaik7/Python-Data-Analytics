

import os
print("Files in folder:", os.listdir("D:\\Pandas-df"))

print(os.getcwd())  # shows your current working directory
print(os.path.exists("Global-Superstore.csv"))  # True if found

import pandas as pd #Import pandas
df = pd.read_csv(r"D:\Pandas-df\Global-Superstore.csv", encoding="latin1") # read.csv returns an panda object
print(df.head())  # show first 5 rows #Understand your data
print(df.shape)       # rows & columns
print(df.columns)     # column names
print(df.info())      # data types
print(df.describe())  # quick statistics
#This is always the first step in any pandas project: Load → Inspect → Explore.



