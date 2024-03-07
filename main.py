import requests
from bs4 import BeautifulSoup as BS

link = "https://dnd.su/race/"
responce = requests.get(link).text
soup = BS(responce, 'lxml')

block = soup.find('div', class_ = "articles-tiles")

result = ""

length = len(block.find_all('span', class_ = "article_title"))

for i in range(length):
    anime = block.find_all('span', class_ = "article_title")[i].text
    result += anime + ", "

print(result)