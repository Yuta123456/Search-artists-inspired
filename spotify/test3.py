from spotify import spotify

name = "ELLEGARDEN"
artists = []
offset = 0
while offset < 1000:
    result = spotify.search(
        q='genre:j-pop', type='artist', limit=50, offset=offset)
    result = result['artists']['items']
    # print(type(result), result.keys())
    for r in result:
        # print(r['name'], r['followers']['total'])
        artists.append([r['name'], r['followers']['total'], r['popularity']])
    offset += 50

artists.sort(key=lambda x: x[1], reverse=True)
print(artists[:100])
# len = 126
# j-pop rock alternative
