import requests
from bs4 import BeautifulSoup

URL= "https://www.billboard.com/charts/hot-100/"
time= input("Wich year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

response= requests.get(URL+ time)
billboard_page= response.text

soup= BeautifulSoup(billboard_page, "html.parser")
song_list = []
songs = soup.select(selector='li ul li h3')
for song in songs:
    song_list.append(song.get_text(strip=True))
print(song_list)
