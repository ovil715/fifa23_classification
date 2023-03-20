import requests
import json
from bs4 import BeautifulSoup
import time

##get text
main_url = "https://www.fifaindex.com/players/"
#
# #there is 605 pages
filepaths = [main_url + f"?page={i+1}" for i in range(605)]

result = {}

for path in filepaths:
    response = requests.get(path)
    source = response.text

    soup= BeautifulSoup(source, "html.parser")
    for row in soup.table.find_all('tr'):
        for a in row.find_all('a'):
            if a.get('class')==["link-player"]:
                name=a.get('title').rstrip(" FIFA 23")
                link=a.get('href')
                link =  "https://www.fifaindex.com/" + link
                result[name]=link
    index = filepaths.index(path)
    print(f"Printed page {index+1} of {len(filepaths)}")
    time.sleep(5)



with open('links_table.json', 'w') as storage_file:
    storage_file.write(json.dumps(result))

