import random
import time

import speech_recognition as sr
import pyttsx3 as pyt


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening")
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def say(engine, text):
    engine.say(text)
    engine.runAndWait()


def populate(PARAMS=[], PROMPT_LIMIT=5):
    # create recognizer and mic instances
    values = {}
    engine = pyt.init()
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()


    for p in PARAMS:
        # ask for params via text to speech
        while True:
            for j in range(PROMPT_LIMIT):
                say(engine, f'Please state your {p}')
                value = recognize_speech_from_mic(recognizer, microphone)
                if value["transcription"]:
                    break
                if not value["success"]:
                    break
                say(engine, "I didn't catch that. What did you say?\n")

            # if there was an error, stop the program
            if value["error"]:
                print("ERROR: {}".format(value["error"]))
                break

            
            say(engine, f"You said: {value['transcription']}. Is this correct?")
            ans = recognize_speech_from_mic(recognizer, microphone)
            print(ans)
            if ans['transcription'] == "yes":
                values[p] = value['transcription']
                break
            else:
                say(engine, f"Let's try again for {p}.")

    print(values)
    say(engine, f"You are {values['first name']} {values['last name']}")

    return values

if __name__ == "__main__":
    #parameters needed to collect
    PARAMS = ["first name", "last name", "street number", "street name", "city"]
    PARAMS = ["first name", "last name"]
    populate(PARAMS, PROMPT_LIMIT=5)


