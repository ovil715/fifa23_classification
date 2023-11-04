import requests
import json
from bs4 import BeautifulSoup
import time

with open("links_table_clean.json", "r") as file:
    links=json.load(file)

timesleep=1

scraped_data = {}

for key, url in links.items():
    response = requests.get(url)
    source = response.text

    soup= BeautifulSoup(source, "html.parser")

    player_dictionary = {}
    for row in soup.find_all("div", class_="card-body"):
        for element in row.find_all("p", class_=""):
            # the ones that have just 1 are descriptions
            if len(element.contents) > 1:
                if element.contents[1].string is None:
                    if element.contents[0] == "Height " or element.contents[0] == "Weight ":
                        player_dictionary[element.contents[0].strip()] = element.contents[1].find("span", class_="data-units data-units-metric").contents[0]
                    elif element.contents[0] == "Weak Foot " or element.contents[0] == "Skill Moves ":
                        #number of stars
                        player_dictionary[element.contents[0].strip()] = len(element.contents[1].find_all("i", class_="fas fa-star fa-lg"))
                    #the only one left should  be Preferred positions: can be multiple
                    else:
                        player_dictionary[element.contents[0].strip()] = []
                        for position in element.contents[1].find_all("a", class_="link-position"):
                            player_dictionary[element.contents[0].strip()].append(position["title"])
                else:
                    content=[content.string for content in element.contents]
                    player_dictionary[content[0].strip()]=content[1]
    print(player_dictionary)
    scraped_data[key] = player_dictionary
    time.sleep(timesleep)

with open('fifa_data.json', 'w') as storage_file:
    storage_file.write(json.dumps(scraped_data))

