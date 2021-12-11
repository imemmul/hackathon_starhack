import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

temp_stores = []

half_response = 'Okay, i took your order i will check whether it is available.'

def speak(text):
    engine.setProperty("rate", 125)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def command_loop():
    try:
        speak("What do you want to order ?")
        order = get_audio()
        if "pizza" in order:
            speak("How do you want your pizza ?")
            order = get_audio()
            if 'pepperoni' in order:
                speak("Okay, do you want any drink ?")
                order = get_audio()
                if 'coke' or 'cola' in order:
                    speak(half_response)
                elif 'sprite' in order:
                    speak(half_response)
            elif 'margarita' in order:
                speak("Okay, do you want any drink ?")
                order = get_audio()
                if 'coke' or 'cola' in order:
                    speak(half_response)
                elif 'sprite' in order:
                    speak(half_response) 

            
            
        
    except:
        pass


def get_audio():
    r = sr.Recognizer()
    text = ''
    with sr.Microphone() as source:
        print("Say something!")
        try:
            audio = r.listen(source, phrase_time_limit=2)
            return (r.recognize_google(audio).lower())
        except TypeError as e:
            print("error; {0}".format(e))


if __name__ =="__main__":
    command_loop()
