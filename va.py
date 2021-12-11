import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    engine.setProperty("rate", 125)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def callback(recognizer, audio):
    try:
        said = recognizer.recognize_google(audio).lower()
        if 'hey' in said:
            speak("I am listening.")
            command = get_audio()
            if 'order' in command:
                speak("What do you want to order ?")
                command = get_audio()
                if "pizza" in command:
                    speak("I like pizza")
    except:
        pass


def get_audio():
    r = sr.Recognizer()
    text = ''
    with sr.Microphone() as source:
        print("Say something!")
        try:
            audio = r.listen(source, phrase_time_limit=2)
            return (r.recognize_google(audio).lower)
        except TypeError as e:
            print("error; {0}".format(e))


if __name__ =="__main__":
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
    print("--- BACKGROUND LISTENING HAS BEEN STARTED ---")
    stop_listening = r.listen_in_background(m, callback=callback)
