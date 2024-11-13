import subprocess

def list_playlists():
    script = f"""
    tell application "System Events"
        do shell script "/usr/bin/env osascript -e 'tell application \\"System Events\\" to click at {{ {700}, {70} }}'"
    end tell
    """
    # script = '''
    # tell application "Rekordbox"
    #     activate
    #     set playlist_names to ""
    #     tell application "System Events"
    #         keystroke "f" using {control down}  -- search collection to unfocus playlist
    #         keystroke "p" using {control down}  -- navigate to playlist section
    #         -- Focus on the playlist pane
    #         key code 48 using {shift down}
    #         -- Start collecting playlist names by navigating through them
    #         key code 125
    #         do shell script "/usr/bin/env osascript -e 'tell application \"System Events\" to click at { " & 130 & ", " & 565 & " }'"
    #     end tell
    #     return playlist_names
    # end tell
    # '''
    # script = '''
    # tell application "Rekordbox"
    #     activate
    #     set playlist_names to ""
    #     tell application "System Events"
    #         keystroke "f" using {control down}  -- search collection to unfocus playlist
    #         keystroke "p" using {control down}  -- navigate to playlist section
    #         -- Focus on the playlist pane
    #         key code 48 using {shift down}
    #         -- Start collecting playlist names by navigating through them
    #         repeat 10 times  -- Adjust the number of iterations as needed
    #             key code 125
    #             keystroke "c" using {command down} -- Copy to clipboard
    #             set playlist_name to (the clipboard as text) -- Get the copied playlist name
    #         end repeat
    #     end tell
    #     return playlist_names
    # end tell
    # '''
    
    # Run the AppleScript and capture the output
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    print(result)
    if result.returncode == 0:
        playlists = result.stdout.strip().split("\n")
        print("Playlists found:")
        for playlist in playlists:
            print(f"- {playlist}")
    else:
        print("Failed to list playlists.")

# Example usage
list_playlists()
