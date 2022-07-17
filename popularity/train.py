import json
import pickle
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

STEP = 30
x = []
y = []
debut_year = []
followers = []
popularity = []
artists_data = json.load(
    open("artists.json", mode="r"))
for artist in artists_data:
    #     {
    #     "popularity": 65,
    #     "debut_year": "1992",
    #     "followers": 2292732,
    #     "name": "No Doubt",
    #     "id": "0cQbJU1aAzvbEmTuljWLlF",
    #     "ranking": "100",
    #     "genres": [
    #       "alternative rock",
    #       "dance pop",
    #       "dance rock",
    #       "permanent wave",
    #       "pop rock"
    #     ]
    #   },
    x.append([
        (2022 - int(artist['debut_year'])) / 122,
        artist['followers'] / 8e+07,
        artist['popularity'] / 100
    ])
    debut_year.append((2022 - int(artist['debut_year'])) / 122)
    followers.append(artist['followers'] / 8e+07)
    popularity.append(artist['popularity'] / 100)
    y.append(10000 - STEP * int(artist['ranking']))
debut_year = pd.DataFrame(debut_year)
followers = pd.DataFrame(followers)
popularity = pd.DataFrame(popularity)
print(debut_year.describe())
print(followers.describe())
print(popularity.describe())
x = pd.DataFrame(x)
y = pd.DataFrame(y)
x.columns = ['debut_year', 'followers', 'popularity']
model = LinearRegression()
model.fit(x, y)
coef = model.coef_
df_coef = pd.DataFrame(*coef, index=x.columns)
print(df_coef)
print(model.score(x, y))

filename = 'model.pkl'
pickle.dump(model, open(filename, 'wb'))
