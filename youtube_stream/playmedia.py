import subprocess, os
from configparser import ConfigParser
from .imports import config_file
def get_path():
    cfg = ConfigParser()
    try:
        cfg.read_string(config_file)
    except:
        return r'{} '.format("vlc")
    if os.name=='nt':
        path = cfg.get("windows", "vlc")
    else:
        path = cfg.get("linux", "vlc")
    return r'{} '.format(path)

def play(videos):
    subprocess.Popen(get_path()+ videos +" 2> /dev/null", shell=True)