import datetime
import json

from popularity.estimate import estimate_score

from spotify_service.spotify import spotify
from spotify_service.util import debut_day_of_artist


rock_artists = json.load(
    open("rock_5000.json", mode="r"))
links = []
nodes = []
save_rl_artists = []
nodes_set = set()
for i, artist in enumerate(rock_artists):
    links = []
    nodes = []
    save_rl_artists = []
    artist_id = artist['id']
    nodes.append({"id": artist['name']})
    related_artists = spotify.artist_related_artists(artist_id)
    for related_artist in related_artists['artists']:
        score = estimate_score(related_artist)
        if score <= 8000:
            continue

        related_artist['debut_year'] = datetime.datetime.strptime(
            debut_day_of_artist(related_artist['id']), "%Y-%m-%d").strftime("%Y")
        # 今は、無条件でエッジを張ってるが、これはグラフがぐちゃぐちゃになる。考える。
        source, target = min([artist, related_artist], key=lambda x: int(x['debut_year'])), \
            max([artist, related_artist], key=lambda x: int(x['debut_year']))
        links.append({
            'weight': 1,
            'source': source['name'],
            'target': target['name']
        })
        # 一応保存
        save_rl_artists.append(related_artist)
        nodes.append({'id': related_artist['name']})
    with open(f"data/links/{artist['name']}_links.json", mode="w") as f:
        json.dump(links, f, indent=4)
    with open(f"data/lr_artists/{artist['name']}_lr_artists.json", mode="w") as f:
        json.dump(save_rl_artists, f, indent=4)
    print(f"{i+1}番目のアーティストまで終了")

graph_json = {
    "directed": True,
    "multigraph": False,
    "graph": {},
    "nodes": nodes,
    "links": links
}
with open('graph_rock.json', 'w') as f:
    json.dump(graph_json, f, indent=4)
with open('related_artists.json', 'w') as f:
    json.dump(save_rl_artists, f, indent=4)
