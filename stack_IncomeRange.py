import pandas as pd
import numpy as np

## Code for "IncomeRange" as the layer.

## This code's end result is to rearrange the data in a table where the first column is the
## "IncomeRange" and the rest of the columns represent the different loan statuses.
## The purpose is to have a data structure (table data) that can be stacked with d3 with the
## "IncomeRange" as the layer.
## The values within each cell of the "LoanStatus" columns will represent the percentage of this
## particular "IncomeRange" row within that "LoanStatus" column.

## Please check FirstVersion.csv (the product of this code) to see what this code
## generates.



## First: importing the the trimmed dataset 

io = pd.read_csv("trimmed_prosper_loan.csv")

## Grouping by by IncomeRange and LoanStatus
## and replacing missing values with 0

df = io[["LoanStatus","IncomeRange",]].copy()

df_new = df.groupby(["IncomeRange","LoanStatus"]).size().unstack("LoanStatus").reset_index().fillna(0)
df_new.columns.name=None
#print(df_new)



## The grouping by done above results in a dataframe (df_new) with 13 columns and 8 rows.
## There are 7 Past Due columns among the above columns


## grouping all the "Past Due" columns under one column by calculating the sum
## of each row. The sum of each each row is appended to the list "L".

n = 0
L = []
while n < 8:
    x = df_new.iloc[n,7:13].sum()
    L.append(x)
    n = n+1

#print(L)

## replacing the values of the column "Past Due (1-15 days)" with the corresponding
## elements in "L".
    
n = 0
while n < 8:
    df_new.iloc[n,7] = L[n]
    n = n + 1

df_final = df_new.iloc[:,0:8]


## removing the "cancelled" column since the values are very low and renaming some
## other columns with a shorter name.

df_final.drop("Cancelled",axis=1,inplace=True)
df_final.rename(columns={"Past Due (1-15 days)":"Past Due","FinalPaymentInProgress":
                         "FinalPayment"},inplace=True)


## looping through each column and generating new a list of values for each column
## where each value represents the percentage of particular "IncomeRange" within
## that "LoanStatus" column.


col=1
row=0
col_lists = [list(df_final["IncomeRange"])]


while col < 7:
    L = []
    for n in range(8):
        cell = round(float(df_final.iloc[n,col])/float(df_final.iloc[:,col].sum())*100.0,2)
        L.append(cell)
        
        
    col = col + 1
    col_lists.append(L)


## rearranging the dataframe so that "IncomeRange" is the first column

df_to_stack = pd.DataFrame({"IncomeRange":col_lists[0],"Chargedoff":col_lists[1],
                    "Completed":col_lists[2],"Current":col_lists[3],
                    "Defaulted":col_lists[4],"FinalPayment":col_lists[5],
                    "Past Due":col_lists[6]})

df_to_stack = df_to_stack[["IncomeRange","Chargedoff","Completed","Current","Defaulted",
           "FinalPayment","Past Due"]]

csv_file = df_to_stack.to_csv("FirstVersion.csv",index=None)





