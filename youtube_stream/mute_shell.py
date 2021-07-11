import os, sys


# Link: https://github.com/spatialaudio/python-sounddevice/issues/11#issuecomment-155836787
'''
It seems to work by running this before each PortAudio call:

devnull = os.open(os.devnull, os.O_WRONLY)
old_stderr = os.dup(2)
sys.stderr.flush()
os.dup2(devnull, 2)
os.close(devnull)

and this immediately afterwards (ideally, in a with statement):

os.dup2(old_stderr, 2)
os.close(old_stderr)
'''


old_stderr = os.dup(2)
def mute_on():
    devnull = os.open(os.devnull, os.O_WRONLY)
    
    sys.stderr.flush()
    os.dup2(devnull, 2)
    os.close(devnull)

def mute_off():
    os.dup2(old_stderr, 2)
    os.close(old_stderr)