import glob
import json

artists_links = []
nodes = []
artists_set = set()
json_path = glob.glob("./data/links/*.json")
for jp in json_path:
    artists_data = json.load(open(jp, mode="r"))
    artists_links += artists_data
    for artist in artists_data:
        artists_set.add(artist["source"])
        artists_set.add(artist["target"])
for a in list(artists_set):
    nodes.append({"id": a})
graph = {
    "directed": True,
    "multigraph": False,
    "graph": {},
    "nodes": nodes,
    "links": artists_links,
}
with open('graph.json', 'w') as f:
    json.dump(graph, f, indent=4)