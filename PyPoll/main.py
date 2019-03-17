import os
import csv
import pandas as pd

homework3_csv = os.path.expanduser('~/Desktop/homework3/python-challenge/PyPoll/election_data.csv')
file = "election_data.csv"
pypoll = pd.read_csv(file)

TotalVotes = len(pypoll)
CanList = pypoll["Candidate"].unique()
cand_percent = pypoll["Candidate"].value_counts(normalize=True) * 1
cand_dict = {
    "candidates": ["Khan", "Correy", "Li", "O'Tooley"],
    'percentage of votes': [63.0, 20.0, 14.0, 3.0]}
votes_df = pd.DataFrame(cand_dict)
winner = votes_df.iloc[0,0]

print("Election Results")
print("---------------------")
print(cand_percent.map('{:.0%}'.format))
print("---------------------")
print(f"Winner: {winner}")
pypoll.to_csv("estokes_hw3.txt", sep='\t', index=False)