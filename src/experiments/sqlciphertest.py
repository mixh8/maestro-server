from pyrekordbox import Rekordbox6Database
from pyrekordbox.db6.tables import DjmdPlaylist

from pytube import YouTube
from ffmpy import FFmpeg
import os
import shutil
import subprocess


from pyrekordbox.db6 import tables

import os



# music_path = "~/Downloads/Coldplay - Viva La Vida (Choujaa & Epsylon Remix) l Release Vinyl.mp3"

# # Define the AppleScript
# applescript_code = f'''
# -- Copy the file path to the clipboard
# set the clipboard to "{music_path}"

# tell application "Rekordbox"
#     activate -- Bring Rekordbox to the front
# end tell

# delay 0.5 -- Wait for Rekordbox to be active

# tell application "System Events"
#     -- Simulate Control + I to open the Import Track dialog
#     keystroke "i" using {{control down}}
    
#     delay 0.5 -- Wait for the dialog to open
#     keystroke "g" using {{command down, shift down}}

#     -- Paste the file path into the dialog
#     keystroke "v" using {{command down}}
#     delay 0.5
#     keystroke return -- Confirm selection
#     delay 0.5
#     keystroke return -- Confirm selection

# end tell
# '''
# applescript_code = f'''
# tell application "Rekordbox"
#     activate -- Bring Rekordbox to the front
# end tell

# delay 1 -- Wait for Rekordbox to be active

# tell application "System Events"
#     -- Simulate Control + I to open the Import Track dialog
#     keystroke "i" using {{control down}}
    
#     delay 3 -- Wait for the dialog to open

#     -- Use the file path to open the file directly
#     keystroke "{music_path}"
#     delay 1
#     keystroke return -- Confirm selection
# end tell
# '''
# Execute the AppleScript using osascript
# subprocess.run(['osascript', '-e', applescript_code])


# Add tracks and sub-playlists (folders)
# pl.add_track(track.TrackID)
# pl.add_playlist("Sub Sub Playlist")

db = Rekordbox6Database()

query = db.query(tables.DjmdContent)
result = query.filter(tables.DjmdContent.Title.contains("Drake Feat. Giveon - Chicago Freestyle (PROVI Remix) l Release Vinyl")).all()
for r in result:
    print(r.Title)

# for r in result:
#     print(r.Title)
# # db.create_playlist("Test Playlist")
# # db.commit()
# # todo use apple script to reload playlist by opening and closing playlist tab

# playlists: DjmdPlaylist = db.get_playlist().all()
# for playlist in playlists:
#     print(playlist.Name)
