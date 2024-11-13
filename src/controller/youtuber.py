import shutil
import subprocess
import googleapiclient.discovery
import dotenv
# from pytube import YouTube, Search
from pytubefix import YouTube, Search
from typing import List
import json
import re
import os
from ffmpy import FFmpeg
from model.ytmodel import YtResult, YtResponse, Response

class Youtuber:
    def __init__(self):
        return

    def search(self, query: str) -> YtResponse:
        """search for a video

        Args:
            query (str): search query

        Returns:
            YtResponse: list of YtResult objects
        """
        videos = self._get_videos(query)
        return videos
    
    def autocomplete(self, query: str):
        search = Search(query)
        return search.completion_suggestions

    def _get_videos(self, query):
        search = Search(query)
        videos: List[YouTube] = search.results
        return [
            YtResult(video.title,
                     video.watch_url,
                     video._author,
                     video.thumbnail_url,
                     ).serialize()
            for video in videos
        ]
    
    def _download_mp3(self, url):
        yt = YouTube(url)
        
        tmp_path = os.getcwd() + "/tmp"
        downloads_path = "/Users/michelmaalouli/Downloads"
        safe_title = re.sub(r'[^a-zA-Z0-9 _-]', '', yt.title)
        full_downloads_path = f"{downloads_path}/{safe_title}.mp3"
        yt.streams.filter(only_audio=True).first().download(tmp_path, safe_title+".mp4")
        file_path = f"{tmp_path}/{safe_title}.mp4"
        if os.path.exists(file_path):
            print(f"File exists: {file_path}")
        else:
            print(f"File not found: {file_path}")
        ff = FFmpeg(inputs={f"{tmp_path}/{safe_title}.mp4": None}, outputs={full_downloads_path: None})
        ff.run()
        os.remove(f"{tmp_path}/{safe_title}.mp4")

        # move to rekordbox collection
        applescript_code = get_applescript_code("~/Downloads/" + safe_title + ".mp3")
        subprocess.run(['osascript', '-e', applescript_code])

        return safe_title


def get_applescript_code(music_path: str):

    return f'''
    -- Copy the file path to the clipboard
    set the clipboard to "{music_path}"

    tell application "Rekordbox"
        activate -- Bring Rekordbox to the front
    end tell

    delay 1 -- Wait for Rekordbox to be active

    tell application "System Events"
        -- Simulate Control + I to open the Import Track dialog
        keystroke "i" using {{control down}}
        
        delay 1 -- Wait for the dialog to open
        keystroke "g" using {{command down, shift down}}
        
        delay 1
        keystroke (ASCII character 8) -- ASCII character 8 represents the backspace key

        -- Paste the file path into the dialog
        keystroke "v" using {{command down}}
        delay 1

        keystroke return -- Confirm selection
        delay 1
        keystroke return -- Confirm selection

    end tell
    '''