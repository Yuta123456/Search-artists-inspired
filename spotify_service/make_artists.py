import requests
from util import debut_day_of_artist
from spotify_service.spotify import spotify
from popularity.estimate import estimate_score
import datetime
import json
from time import sleep

artists = []
offset = 0
while offset < 1000:
    result = spotify.search(
        q='genre:rock', type='artist', limit=50, offset=offset)
    result = result['artists']['items']
    result = filter(lambda x: estimate_score(x) > 8000, result)
    for artist in result:
        name = artist['name']
        debut_year = datetime.datetime.strptime(
            debut_day_of_artist(artist['id']), "%Y-%m-%d").strftime("%Y")
        new_artist = {
            'popularity': artist['popularity'],
            'debut_year': debut_year,
            'followers': artist['followers']['total'],
            'name': artist['name'],
            'id': artist['id'],
            'genres': artist['genres']
        }
        artists.append(new_artist)
    offset += 50
    print("{:.2f} % : ".format(len(artists)*100/5000), datetime.datetime.now())
    sleep(2)

with open('rock_5000.json', 'w') as f:
    json.dump(artists, f, indent=4)
