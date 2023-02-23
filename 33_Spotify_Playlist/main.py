import requests
from bs4 import BeautifulSoup
from decouple import config
import spotipy

date_for_songs = input("What time do you want to travel to? Please enter in the format YYYY-MM-DD: ")
# date_for_songs = "2022-01-14"

try:
    web_page = requests.get(f"https://www.billboard.com/charts/hot-100/{date_for_songs}/"). \
        text.encode('unicode_escape').decode()
    soup = BeautifulSoup(web_page, "html.parser")
except Exception as ex_:
    print(ex_)
else:
    # Get the details for a song by scraping the website
    li = soup.find_all(class_="lrv-u-width-100p", name="li")
    song_list = []
    for one in li:
        try:
            ul = one.find(class_="lrv-a-unstyle-list", name="ul")
            song_con = ul.find(class_="o-chart-results-list__item", name="li")
            song_li = song_con.find(id="title-of-a-story", name="h3", class_="c-title")
            artist = song_con.find(name="span", class_="c-label").text.strip().replace("\\n", "").replace("\\t", "")
            song = song_li.text.strip().replace("\\n", "").replace("\\t", "")
            song_info = {
                "name": song,
                "artist": artist,
                "year": date_for_songs[:4]
            }
        except Exception as ex:
            pass
        else:
            song_list.append(song_info)
    # print(song_list)

    ## Spotify connection
    spotify = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyOAuth(
        client_id=config("SPOTIPY_CLIENT_ID"),
        client_secret=config("SPOTIPY_CLIENT_SECRET"),
        scope="playlist-modify-private",
        redirect_uri=config("SPOTIPY_REDIRECT_URI")
    ))

    user_id = spotify.current_user()["id"]

    # Convert song names to uris
    song_uris = []
    for song in song_list:
        try:
            query = f'track:{song.get("name")} artist:{song.get("artist")} year:{song.get("year")}'
            # Search for track on Spotify
            results = spotify.search(q=query, type='track', limit=1)
            song_uri = results['tracks']['items'][0]['id']
        except:
            pass
        else:
            song_uris.append(song_uri)

    # print(song_uris)
    # song_uris = ['717iS0iKM4ARyATicoitTh', '4AmCmEjyXlwulMN2QMUx5D', '6SR8tWgGvYoA2VJDgPQSWo', '66nNMbwyH4N3vqEZ7E4Z8n', '7vrKEP66NdiQDPryPG6olO', '1Y5Jvi3eLi4Chwqch9GMem', '2IcKt8tzrR6TC73T1N4yi9', '32o0KgIZ82kx1V7SQpm226', '6K5ph5mq1qprHae3TrgTj5', '3pBMxsy5HwmqpsZsT7YLqv', '58UKC45GPNTflCN6nwCUeF', '1cpRzJejddTExQeVW14UhU', '3Z9iVaKGEDZtd6jvzuoF0e', '2psUZ3pOZZ95FHLgPvWv05', '0RZkkGU4tQ6IxmERzX32cl', '2tQmOuBx8cSjdKYLKboYHt', '2aJnyNu4PQxQ2lyj5boiMG', '3ncmoWTwJgx63LwMTyBCXf', '4hpWtPnZHX9xfb1fr8cVVw', '0fYuP6BSJlSJsCeorXOBfx', '3EYuJUqcmLFIeEnYCioHV7', '5ekA7j4MPQa3NZbZQSpRfF', '6afydtzpO5ttLXO57HWe4g', '4pi1G1x8tl9VfdD9bL3maT', '1ik2NJRkLcMPYImIMuRUTg', '40F9BdNeGSLbfnD2vtigMX', '4oraAnnNob8laF6jEKWPE5', '1u4HUiREUR6vX1W1RYG2Tm', '602UZCVSrztI6PhqSxlpPD', '6aZVQQUl17WqobPx0UZKxo', '6xcFBFyO9Q21SLmifyA2vi', '4I20dwCQ6haFbw02LlhjC6', '1TlTzdsEpgfsmbuNfYmWfG', '1zIzd27gmbNrWWkMCEWmgC', '5gUiTylvifZnUrynE4FFPu', '4ckr69xqnvlU38D4CfPfLs', '3yMC1KsTwh0ceXdIe4QQAQ', '6cwLio1ZAMePxIZSEb3hxa', '2Zohe4YtPmvPZWSE0ABCzU', '6TEcZu2qQSsC40T7qV18lB', '4EVb8k6IMtHD4c9n0ub5vk', '6TpyujRefwsflWFXbmjVpj', '1X8E4vVoOM3BpSQlEDSjjM', '3JfhLEO8qB9qZr9xIefh5m', '0IMUFRaM2W3wKNM1CSQ4Zm', '3sfQu8ixdx7IHvoEVwnx8s', '3A3S5pdCJdePtJ0oKeCrCP', '6aIrXGmaFqPafbYgxbMUsj', '0JddOFuDiG5MFyQ82lGDcL', '1hB3M3POeKMLxcEFEvPeqU', '40MXr7BMh3ShPf2b9giSRt', '1nweeyStisj4PB4w037yzO', '0F6XcWEzymSracgq12pOXX', '5pNKUZrtIHC25ESDXC3b1A', '6u5z7SHWYAPB38SUenzZK1']

    # Define playlist name and description
    playlist_name = f'{date_for_songs} Top 100 Billboard'
    playlist_description = 'Top 100 Billboard songs of the week.'

    # Create new playlist on Spotify
    playlist = spotify.user_playlist_create(user=user_id, name=playlist_name, public=False,
                                            description=playlist_description)

    # Add tracks to playlist
    spotify.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
