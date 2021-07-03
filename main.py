import re, subprocess, urllib.parse, urllib.request, sys
from bs4 import BeautifulSoup
import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response


def voice():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print('Listening...')
    voice_text = recognize_speech_from_mic(recognizer, microphone)
    if voice_text["transcription"]:
        print(voice_text['transcription'])
        return voice_text['transcription']

    if not voice_text["success"]:
        print("I didn't catch that. What did you say?\n")
        exit()
    if voice_text["error"]:
        print("ERROR: {}".format(voice_text["error"]))
        exit()




def stream(music_name):
    query= urllib.parse.urlencode({"search_query": music_name})
    searchUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query)
    search_results = re.findall(r"watch\?v=(\S{11})", searchUrl.read().decode())
    video = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

    subprocess.Popen(
    "cvlc "+" --play-and-exit "+ video +" vlc://quit", #+ " --no-video --loop=inf --input-ipc-server=\\\\.\\pipe\\mpv-pipe > output.txt"
    shell=True)
    exit()



if len(sys.argv)>1:
    music_name = " ".join(sys.argv[1:])
    stream(music_name)

else:
    music_name=voice()
    stream(music_name)
