import sys
from .distrun import run
from .voice_recognition import voice
from .search import search
from .playmedia import play

def main():
    if sys.argv[0][-4:]=='.exe': # For Windows .exe file!
        run()

    elif len(sys.argv)>1:   # For linux
        music_name = " ".join(sys.argv[1:])
    else:
        music_name=voice()

    if music_name is not None:
        videos = search(music_name)
        play(videos)

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('See you again!')
        sys.exit(0)