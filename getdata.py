import requests
import json
from bs4 import BeautifulSoup
import time

#testcase
# playerurl = "https://www.fifaindex.com/player/231747/kylian-mbapp%C3%A9/"
#
# response = requests.get(playerurl)
# source = response.text
#
# ##save the response to work later
# with open("mbappe.txt","w", encoding="utf-8") as file:
#     file.write(source)


#card-body
#badge badge-dark rating r1

with open("mbappe.txt","r",encoding="utf-8") as file:
    source = file.read()

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
# insert dictionary to sql