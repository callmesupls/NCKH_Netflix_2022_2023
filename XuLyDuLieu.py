import os
import numpy as np
import pandas as pd
netflix_titles = pd.read_csv('netflix_titles.csv')
print(len(netflix_titles))
for i in netflix_titles.columns:
  print(netflix_titles[i].isna().sum())