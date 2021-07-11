import speech_recognition as sr
from .mute_shell import mute_on, mute_off
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
    mute_on()
    microphone = sr.Microphone()
    mute_off()

    print('Listening... (Press "Ctrl+C" to cancel)')
    voice_text = recognize_speech_from_mic(recognizer, microphone)

    if voice_text["transcription"]:
        print(voice_text['transcription'])
        return voice_text['transcription']

    if not voice_text["success"]:
        print("I didn't catch that. What did you say?\n")
    if voice_text["error"]:
        print("ERROR: {}".format(voice_text["error"]))
    