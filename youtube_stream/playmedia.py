import subprocess, os
from configparser import ConfigParser
from importlib import resources  # Python 3.7+

def get_path():
    cfg = ConfigParser()
    cfg.read_string(resources.read_text("youtube_stream", "config.txt"))
    if os.name=='nt':
        path = cfg.get("windows", "vlc")
    else:
        path = cfg.get("linux", "vlc")
    return r'{} '.format(path)

def play(videos):
    subprocess.Popen(get_path()+ videos, shell=True)