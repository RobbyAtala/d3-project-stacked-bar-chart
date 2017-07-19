import csv
import pandas as pd

## the "prosperLoanData.csv" is the original file with 113k loans datafile.
## I trimmed this huge csv and selected a few columns of interest for my
## project.

df = pd.read_csv("prosperLoanData.csv",
                 usecols=["LoanStatus","Occupation","CreditScoreRangeLower",
                        "CreditScoreRangeUpper","DelinquenciesLast7Years",
                    "LoanOriginalAmount","IncomeRange","DebtToIncomeRatio"])


trimmed_csv = df.to_csv("/Users/rab/Downloads/trimmed_prosper_loan.csv")


## "trimmed_prosper_loan.csv" will be later used to generate a data table to be
## stacked with d3.
