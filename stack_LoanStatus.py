import pandas as pd
import numpy as np

## Code for "LoanStatus" as the layer.


## This code's end result is to rearrange the data in a table where the first column is the
## "LoanStatus" and the rest of the columns represent the different "IncomeRange"s.
## The purpose is to have a data structure (table data) that can be stacked with d3 with the
## "LoanStatus" as the layer.
## The values within each cell of the "IncomeRange" columns will represent the percentage of this
## particular "LoanStatus" row within that "IncomeRange" column.

## Please check SecVersion.csv (the product of this code) to see what this code
## generates.


## First: importing the the trimmed dataset

io = pd.read_csv("trimmed_prosper_loan.csv")

## Grouping by by LoanStatus and IncomeRange
## and replacing missing values with 0

df = io[["LoanStatus","IncomeRange",]].copy()

df_new = df.groupby(["LoanStatus","IncomeRange"]).size().unstack("IncomeRange").reset_index().fillna(0)
df_new.columns.name=None
#print(df_new)

## combining all the "Past Due" rows into one row by summing each "non-LoanStatus"
## column from row 6 to row 11 and appending the values to the list "L".

n = 1
L = []
while n < 9:
    x = df_new.iloc[6:12,n].sum()
    L.append(x)
    n = n+1

##print(L)

## replacing the values of the row "Past Due (1-15 days)" with the corresponding
## elements in "L".

n = 1
while n < 9:
    df_new.iloc[6,n] = L[n-1]
    n = n + 1

df_final = df_new.iloc[0:7,:]
#print(df_final)

## removing the "cancelled" row since its values are negligible and renaming
## the "string" values of rows 5 and 6 of the "LoanStatus" column with shorter
## "string"s.

shortDF = df_final.copy()
shortDF.drop(0,axis=0,inplace=True)
shortDF.replace(["FinalPaymentInProgress","Past Due (1-15 days)"],["Last Payment","Past Due"
],inplace=True)

#print(shortDF)

## looping through each column and generating new a list of values for each column
## where each value represents the percentage of particular "LoanStatus" within
## that "IncomeRange" column.


col=1
col_lists = [list(shortDF["LoanStatus"])]

while col < 9:
    L = []
    for n in range(6):
        cell = round(float(shortDF.iloc[n,col])/float(shortDF.iloc[:,col].sum())*100.0,2)
        L.append(cell)
        
        
    col = col + 1
    col_lists.append(L)
    

## rearranging the dataframe so that "LoanStatus" is the first column

df_to_stack = pd.DataFrame({"LoanStatus":col_lists[0],"$0":col_lists[1],
                    "$1-24999":col_lists[2],"$100000+":col_lists[3],
                    "$25000-49999":col_lists[4],"$50000-74999":col_lists[5],
                    "$75000-99999":col_lists[6],"Not displayed":col_lists[7],
                    "Not employed":col_lists[8]})

df_to_stack = df_to_stack[["LoanStatus","$0","$1-24999","$25000-49999","$50000-74999",
                           "$75000-99999","$100000+","Not displayed","Not employed"]]

#print(df_to_stack)

csv_file = df_to_stack.to_csv("SecVersion.csv",index=None)





