import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv

#loading environment variables
load_dotenv("./spotify_playlist/.env")
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID") 
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

#user input for date
print("Lets go back in time and get the top 100 music")
date = input("Enter a date (yyyy-mm-dd): ")

billboard = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

#scrape billboard to get the songs list
billboard_soup = BeautifulSoup(billboard.text, "html.parser")
songs = billboard_soup.select("li ul li h3")
song_list = []
for song in songs:
    song_list.append(song.getText().strip()) 

#spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope = "playlist-modify-private",
                                               ))


user_id = sp.current_user()["id"]

#go through the songs list and collect their uri one by one
print("Collecting Songs...")
uri_list = []
year = date.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}",type="track")
    uri = result["tracks"]["items"][0]["uri"]
    uri_list.append(uri)

#create a playlist
print(f"{len(uri_list)} songs found")
print("Now creating your playlist")
user_playlist = sp.user_playlist_create(user="31vvdbi7xmdqfdno4wrqqfb6fym4", name=f"Billboard 100 on {date}", public=False)

#add songs to the playlist
print("Almost done adding ( •̀ ω •́ )✧")
sp.playlist_add_items(playlist_id=user_playlist["id"], items=uri_list)

