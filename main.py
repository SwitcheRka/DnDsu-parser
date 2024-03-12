import requests
from bs4 import BeautifulSoup as BS
import os

link = "https://dnd.su/race/"
responce = requests.get(link).text
soup = BS(responce, 'lxml')

block = soup.find('div', class_ = "articles-tiles")

result = ""

length = len(block.find_all('span', class_ = "article_title"))

for i in range(length):
    anime = block.find_all('span', class_ = "article_title")[i].text
    result += anime + ", "

def create_file(result):
    my_file = open("DnDsu_races.txt", "w+")
    my_file.write(result)
    fileContents = my_file.read()
    print(fileContents)
    my_file.close()


create_file(result)