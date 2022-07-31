import json

filename = "graph.json"
artists_year = {}
with open(filename, "r") as f:
    d = json.load(f)
with open("./rock_5000.json", "r") as f:
    rock = json.load(f)
artists_year = {}
for artist in rock:
    name = artist["name"]
    # print(artist)
    artists_year[name] = int(artist["debut_year"])
    try:
        with open(f"./data/lr_artists/{name}_lr_artists.json", "r") as f:
            lr_artists = json.load(f)
    except:
        pass
    for lr in lr_artists:
        name = lr["name"]
        artists_year[name] = int(lr["debut_year"])
with open("./artists_year.json", "w") as f:
    json.dump(artists_year, f)
