import json

filename = "graph_di.json"

with open(filename, "r") as f:
    df = json.load(f)
new_links = []
for edge in df["links"]:
    if edge["source"] != edge["target"]:
        new_links.append(edge)

df["links"] = new_links

with open("graph.json", "w") as f:
    json.dump(df, f)
