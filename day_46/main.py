# Imports
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime


# Get the website content
day = ""
valid_date = True
while valid_date:
    try:
        day = input("Which date do you want to travel in time? \n"
                    "Type it in formar YYYY-MM-DD")
        datetime.strptime(day, '%Y-%m-%d')
        valid_date = False
    except ValueError:
        print("Formato de fecha inválido. Se requiere YY-MM-DD")

url = f"https://www.billboard.com/charts/hot-100/{day}/"
response = requests.get(url).text

# Spotify data
redirect_uri = 'http://example.com'
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SECRET_ID,
        client_secret=SECRET_CLIENT,
        show_dialog=True,
        cache_path="token.txt"
    )
)
results = spotify.artist_top_tracks(redirect_uri)
print(results)

# Make soup
soup = BeautifulSoup(response, "html.parser")
songs_titles_tags = soup.findAll(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                                   "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                                   "u-line-height-normal@mobile-max a-truncate-ellipsis "
                                                   "u-max-width-330 "
                                                   "u-max-width-230@tablet-only")
song_names = [song.getText().replace("\n", "") for song in songs_titles_tags]
print(song_names)
