import requests
from bs4 import BeautifulSoup

TOP_MOVIES_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
web_page = requests.get(TOP_MOVIES_URL).text.encode('unicode_escape').decode()

soup = BeautifulSoup(web_page, "html.parser")
movies = soup.find_all(class_="title", name="h3")

with open("top_movies.txt", "w") as file:
    for movie in reversed(movies):
        file.write(f"{movie.text} \n")
