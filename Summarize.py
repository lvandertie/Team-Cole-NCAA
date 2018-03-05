import pandas as pd
import numpy as np

df = pd.read_csv('DataFiles/RegularSeasonDetailedResults.csv')



print(df.groupby(['Season', 'WTeamID']).mean())
