from spotify import spotify


name = "ELLEGARDEN"
results = spotify.search(q='artist:' + name, type='artist')
print(results.keys())
id = results['artists']['items'][0]['id']
results = spotify.artist(id)
print(dir(results), type(results))
print()
print(results)
# spotify.artist_related_artists(results[])
