import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    engine.setProperty("rate", 125)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
    # OSX may use 48KHz instead of 44KHz ?
        print("Say something!")
        try:
            audio = r.listen(source, phrase_time_limit=2)
            print(r.recognize_google(audio))
        except TypeError as e:
            print("error; {0}".format(e))


def callback(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said" + recognizer.recognize_google(audio))
        if "pizza" in text.lower():
            speak("Hi, Emir")
    except (sr.UnknownValueError, sr.RequestError):
        speak("Sorry, I couldn't hear.")


if __name__ =="__main__":
    #get_audio()
    pass