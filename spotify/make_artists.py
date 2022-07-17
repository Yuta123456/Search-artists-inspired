import datetime
import json
from spotify import spotify
from util import debut_day_of_artist

artists = []
offset = 0
while offset < 100:
    result = spotify.search(
        q='genre:j-pop', type='artist', limit=50, offset=offset)
    result = result['artists']['items']
    result = filter(lambda x: x['popularity'] > 40, result)
    # print(type(result), result.keys())
    for artist in result:
        name = artist['name']
        print(name)
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

with open('test_jpop.json', 'w') as f:
    json.dump(artists, f, indent=2)
