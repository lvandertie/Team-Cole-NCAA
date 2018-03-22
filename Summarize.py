import pandas as pd
import numpy as np

df = pd.read_csv('DataFiles/RegularSeasonDetailedResults.csv')


# Select columns for regression
winners = df[['Season','WTeamID', 'WScore', 'WAst']]
# Rename columns
winners = winners.rename(columns={'WTeamID': 'TeamID', 'WScore': 'Score', 'WAst' : 'Assist'})

losers = df[['Season', 'LTeamID', 'LScore', 'LAst']]
losers = losers.rename(columns={'LTeamID': 'TeamID', 'LScore': 'Score', 'LAst' : 'Assist'})

total = pd.concat([winners, losers])

total = total.groupby(['Season', 'TeamID']).mean()

print(total)


