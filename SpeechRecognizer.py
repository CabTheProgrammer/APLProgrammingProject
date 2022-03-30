# You should install the speech recognizer then import it

import speech_recognition as recognizer
# import playsound


# Then install pyaudio to be able to use any audio
# Maybe optional.


def get_audio():
    rec = recognizer.Recognizer()
    with recognizer.Microphone() as source:
        audio = rec.listen(source)
        said = ""

        try:
            said = rec.recognize_google(audio)
            print(said)
        except Exception as e:  # This is so that if you get an error from not hearing for a while or whatever
            # Else, it doesn't crash the program!!!!
            print("Error with the recognizer! Please restart recognizer." + str(e))
            # Error, you will only have the blank string as detailed above.
    return said



