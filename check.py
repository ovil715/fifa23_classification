import json
with open("links_table_clean.json", "r") as links:
    linkdict=json.load(links)

print(len(linkdict.keys()))

with open("fifa_data.json", "r") as data:
    datadict=json.load(data)

print(len(datadict.keys()))