import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response= requests.get(URL)
empireon_page= response.text

soup= BeautifulSoup(empireon_page, "html.parser")

name_films= soup.find_all(name= "h3", class_= "title")

films= [name.getText() for name in name_films]
films_a= films[::-1]
with open(r"D:\100_Days_of_Python\Web-Scraping\Day45_Web-Sccraping-w-BeautifulSoup\Starting Code - 100 movies to watch start\namefilm.txt","w", encoding="utf-8" ) as file:
    for film in films_a:
        file.write(f"{film} \n")
