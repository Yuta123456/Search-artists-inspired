import json
import pickle
import pandas as pd
model = pickle.load(open("model.pkl", 'rb'))

artists_data = json.load(
    open("test_jpop.json", mode="r"))
for artist in artists_data:
    x = [[
        (2022 - int(artist['debut_year'])) / 122,
        artist['followers'] / 8e+07,
        artist['popularity'] / 100
    ]]
    x = pd.DataFrame(x)
    score = model.predict(x)
    print(artist['name'], score[0][0])
