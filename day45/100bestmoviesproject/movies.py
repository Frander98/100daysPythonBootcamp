from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL).text
soup = BeautifulSoup(response, "html.parser")
movie_titles_text = [movie.getText() for movie in soup.findAll(name="h3", class_="title")]
# reverse the order to get it from 1 to 100
movie_titles_text = movie_titles_text[::-1]

with open("best_movies.txt", "w") as file:
    for movie in movie_titles_text:
        file.write(movie + "\n")

