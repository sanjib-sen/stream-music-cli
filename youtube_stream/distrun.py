from .voice_recognition import voice
from importlib import resources
from .search import search
from .playmedia import play
import sys
from .imports import ascii_art
''' 
 to generate .exe file
 pyinstaller dist.py --add-data "youtube_stream/*.txt;youtube_stream" --onefile --name youtube_stream
 or pyinstaller youtube_stream.spec
 
'''
def run():
    print("\n\n")
    try:
        print(ascii_art)
    except:
        print("             Youtube-Stream      ")
    print("\n\n\n")
    while True:
        print("Type Song name (Use comma (,) for multiple songs)")
        print("Or Press ENTER for Voice Recognition. Say 'then', or 'plus' for multiple songs")
        print("Song Name: ",end ="")

        try:
            music_name = input()
        except KeyboardInterrupt:
            print('\nClose VLC to exit this program.')
            sys.exit(0)

        if len(music_name)==0:
            music_name = voice()
        if music_name is not None:
            videos = search(music_name)
            play(videos)
        print("Started Playing...\n\n")