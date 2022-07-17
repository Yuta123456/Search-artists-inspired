import datetime
import json
import pickle
import pandas as pd

from spotify_service.util import debut_day_of_artist
model = pickle.load(open("model.pkl", 'rb'))

artists_data = json.load(
    open("test_jpop.json", mode="r"))


def estimate_score(artist):
    artist['debut_year'] = datetime.datetime.strptime(
        debut_day_of_artist(artist['id']), "%Y-%m-%d").strftime("%Y")
    x = [[
        (2022 - int(artist['debut_year'])) / 122,
        artist['followers']['total'] / 8e+07,
        artist['popularity'] / 100
    ]]
    x = pd.DataFrame(x)
    score = model.predict(x)
    return score[0][0]
