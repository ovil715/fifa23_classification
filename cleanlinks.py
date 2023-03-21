#housekeeping: the links we got from getlinks.py are badly formatted
import json

with open("links_table.json","r") as file:
    data=json.load(file)

for key in data:
    data[key]=data[key].replace(".com//", ".com/")

with open('links_table_clean.json', 'w') as storage_file:
    storage_file.write(json.dumps(data))

