import pandas as pd
import numpy as np

regular_season_data = pd.read_csv("/Users/coleheflin/Documents/Men's NCAA Competition/DataFiles/RegularSeasonDetailedResults.csv")
tournament_data = pd.read_csv("/Users/coleheflin/Documents/Men's NCAA Competition/DataFiles/NCAATourneyCompactResults.csv")

tournament_data = tournament_data[tournament_data['Season'] >= 2003]
#print(tournament_data)

# Select columns for regression
winners = regular_season_data[['Season','WTeamID', 'WScore', 'WAst']]
# Rename columns
winners = winners.rename(columns={'WTeamID': 'TeamID', 'WScore': 'Score', 'WAst' : 'Assist'})

losers = regular_season_data[['Season', 'LTeamID', 'LScore', 'LAst']]
losers = losers.rename(columns={'LTeamID': 'TeamID', 'LScore': 'Score', 'LAst' : 'Assist'})

total = pd.concat([winners, losers])

total = total.groupby(['Season', 'TeamID'], as_index=False).mean()
total = total.rename(columns={'Score' : 'PPG', 'Assist' : 'APG'})

winner_df = pd.merge(tournament_data, total,  how='inner', left_on=['Season','WTeamID'], right_on = ['Season','TeamID'])
winner_df.drop(['TeamID'], inplace=True, axis=1)

tournament_stats = pd.merge(winner_df, total,  how='inner', left_on=['Season','LTeamID'], right_on = ['Season','TeamID'], suffixes=('_W', '_L'))
tournament_stats.drop(['TeamID'], inplace=True, axis=1)
print(tournament_stats)


