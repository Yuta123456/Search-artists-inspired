from spotify_service import spotify

name = "ELLEGARDEN"
results = spotify.search(q='artist:' + name, type='artist')
print(results.keys())
id = results['artists']['items'][0]['id']
results = spotify.artist_related_artists(id)
# print(len(results['artists']))
# dict_keys(['external_urls', 'followers', 'genres', 'href', 'id', 'images', 'name', 'popularity', 'type', 'uri'])
for artist in results['artists']:
    print(artist['name'])
# spotify.artist_related_artists(results[])

print(len(spotify.artist_albums(id)['items']))
for album in spotify.artist_albums(id)['items']:
    print(album['name'])
