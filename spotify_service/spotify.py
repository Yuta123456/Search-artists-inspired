import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'f815b9bf5e4a4421ba8cb3da7aa796f4'
client_secret = '11e749caf78f4d3fb215e5f7fe45068d'
client_credentials_manager = SpotifyClientCredentials(
    client_id, client_secret)
spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager)