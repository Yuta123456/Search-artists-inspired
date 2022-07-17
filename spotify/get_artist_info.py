import datetime
from spotify import spotify
from util import debut_day_of_artist
import json

ranking_data = json.load(
    open("./popularity/best_artist_ranking/ranking.json", mode="r"))
artists = []
for artist in ranking_data:
    name = artist['name']
    result = spotify.search(q="artist:" + name, type='artist', limit=50)
    result = result['artists']['items']
    result = max(result, key=lambda x: x['popularity'])
    # print(result)
    # print(r['name'], r['followers']['total'])
    print(name)
    debut_year = datetime.datetime.strptime(
        debut_day_of_artist(result['id']), "%Y-%m-%d").strftime("%Y")
    artist['debut_year'] = debut_year
    new_artist = {
        'popularity': result['popularity'],
        'debut_year': debut_year,
        'followers': result['followers']['total'],
        'name': artist['name'],
        'id': result['id'],
        'ranking': artist['Ranking'],
        'genres': result['genres']
    }
    artists.append(new_artist)
with open('test.json', 'w') as f:
    json.dump(artists, f, indent=2)

