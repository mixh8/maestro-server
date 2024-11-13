import time
from flask import Response
from pyrekordbox import Rekordbox6Database
from pyrekordbox.db6.tables import DjmdPlaylist, DjmdContent
from pyrekordbox.db6 import tables
from typing import List


class RekordBoxer():
    def __init__(self):
        return

    def get_playlists(self) -> List[str]:
        """gets names of rekordbox playlists

        Returns:
            List[str]: playlists names
        """
        db = Rekordbox6Database()
        playlists: DjmdPlaylist = db.get_playlist().all()
        return [playlist.Name for playlist in playlists]
    
    def add_song(self, name: str, playlist_name: str):
        """adds a song to a playlist

        Args:
            path (str): name of the song
            playlist (str): playlist name

        Returns:
            Response: response object
        """
        db = Rekordbox6Database()
        print(name, playlist_name)
        query = db.query(tables.DjmdContent)
        time.sleep(2)
        record = query.filter(tables.DjmdContent.Title == name).all()[0]
        playlist = db.get_playlist(Name=playlist_name).one()

        db.add_to_playlist(playlist, record)
        print("ADDED")

        db.commit()
        return name + " added to " + playlist_name

        

    