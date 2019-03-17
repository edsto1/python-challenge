#Eddie Stokes PyBank HW3

#import csv file
import os
import csv
import pandas as pd

homework3_csv = os.path.expanduser('~/Desktop/homework3/python-challenge/PyBank/budget_data.csv')
file = "budget_data.csv"
budget_pd = pd.read_csv(file)

Months = len(budget_pd)
PLtotal = budget_pd["Profit/Losses"].sum()
MonthlyDiff = budget_pd["Profit/Losses"].diff()
MonthlyChange = MonthlyDiff.dropna(how='any')
AvgChange = MonthlyChange.mean()
AvgChangeMax = MonthlyChange.max()
AvgChangeMin = MonthlyChange.min()

print(f'Total Months: {Months}')
print(f'Net Profit/Losses: {PLtotal}')
print(f'Average Monthly Change: {AvgChange}')
print(f'Greatest Increase: {AvgChangeMax}')
print(f'Greatest Decrease: {AvgChangeMin}')
budget_pd.to_csv("estokes_hw3_pybank.txt", sep='\t', index=False)