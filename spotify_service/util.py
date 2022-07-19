import datetime
from spotify_service.spotify import spotify


def debut_day_of_artist(artist_id):
    albums = []
    # ごめんなさい。
    result_album = True
    offset = 0
    while result_album:
        result_album = spotify.artist_albums(
            artist_id, limit=50, offset=offset)['items']
        offset += 50
        albums += result_album
    # print(albums)
    albums = list(filter(lambda x: int(
        x['release_date'].split('-')[0]) > 1900, albums))
    # print(artist_id, albums)
    if len(albums) == 0:
        return "2022-01-01"
    debut_year_album = min(albums, key=lambda x: x['release_date'])
    release_date = debut_year_album['release_date']
    if len(release_date.split('-')) < 3:
        release_date += "-01" * (3 - len(release_date.split('-')))
    # print(release_date, debut_year_album)
    return release_date


def get_popularity_based_on_date(artist_id):
    artist = spotify.artist(artist_id)
    popularity = artist['popularity']
    debut_day = debut_day_of_artist(artist_id)
    debut_year = datetime.datetime.strptime(
        debut_day, "%Y-%m-%d").strftime("%Y")
    this_year = datetime.date.today().strftime("%Y")
    sub = int(this_year) - int(debut_year)
    print(this_year, debut_day)


# get_popularity_based_on_date("3cbd5GWGOknxmFAe77MDbk")
# debut_day_of_artist("2DaxqgrOhkeH0fpeiQq2f4")
