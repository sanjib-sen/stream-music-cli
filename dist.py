from youtube_stream.__main__ import main
''' 
 to generate .exe file
 pyinstaller dist.py --add-data "youtube_stream/*.txt;youtube_stream" --onefile --name youtube_stream
 or pyinstaller youtube_stream.spec
 
'''
if __name__ == '__main__':
    main()