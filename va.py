import pyttsx3
import speech_recognition as sr
import csv
import pandas as pd
import api


engine = pyttsx3.init()

selected_order_type = {'food_type': None, 'food_kind': None, 'drink': None}
dict_car = {'order_id': 1, 'order_type': None, 'latitude': 10, 'longtitude': 20}
dict_store = [{'name':'Starbucks', 'latitude':30.5, 'longtitude':50.5, 'duration':0.5}, {'name':'Burger', 'latitude':20.5, 'longtitude':35.5, 'duration':35}]
csv_columns_store = ['name', 'latitude', 'longtitude', 'duration']
csv_columns_car = ['order_id', 'order_type', 'latitude', 'longtitude']

half_response = 'Okay, i took your order i will check whether it is available.'



def speak(text):
    engine.setProperty("rate", 125)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def command_loop_drink():
    # order = get_audio()
    # if 'coke' or 'cola' in order:
    #     speak(half_response)
    #     selected_order_type['drink'] = 'cola'
    # elif 'sprite' in order:
    #     speak(half_response)
    #     selected_order_type['drink'] = 'sprite'
    # print(selected_order_type)
    save_order_type()

def command_loop_food():
    try:
        # speak("What do you want to order ?")
        # order = get_audio()
        # if "pizza" in order:
        #     speak("How do you want your pizza ?")
        #     selected_order_type['food_type'] = 'pizza'
        #     order = get_audio()
        #     if 'pepperoni' in order:
        #         speak("Okay, do you want any drink ?")
        #         selected_order_type['food_kind'] = 'pepperoni'
        #         command_loop_drink()
        #     elif 'margarita' in order:
        #         speak("Okay, do you want any drink ?")
        #         selected_order_type['food_kind'] = 'margarita'
        #         command_loop_drink()
        selected_order_type['food_type'] = 'pizza'
        selected_order_type['food_kind'] = 'margarita'
        selected_order_type['drink'] = 'cola'
        command_loop_drink()
    except:
        pass

def save_order_type():
    dict_car['order_type'] = selected_order_type
    print(dict_car)
    write_csv('data_car.csv')
    

def write_csv(filename):
    dict_car['order_type'] = dict_car['order_type'].items()
    pd.DataFrame.from_dict(data=dict_car).to_csv(filename)
    api.main()
    

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        try:
            audio = r.listen(source, phrase_time_limit=1.5)
            return (r.recognize_google(audio).lower())
        except TypeError as e:
            print("error; {0}".format(e))


if __name__ =="__main__":
    command_loop_food()
