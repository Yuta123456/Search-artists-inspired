import json

filename = "graph.json"
with open(filename, "r") as f:
    d = json.load(f)
links = []
with open("artists_year.json", "r") as f:
    year = json.load(f)
for link in d["links"]:
    s = link["source"]
    t = link["target"]
    s_key = (((year[s] % 100) // 10) - 3) % 10
    t_key = (((year[t] % 100) // 10) - 3) % 10
    if s_key + 1 == t_key:
        links.append(link)
d["links"] = links

with open("graph_filtered.json", "w") as f:
    json.dump(d, f)
