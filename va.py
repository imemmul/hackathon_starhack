import pyttsx3
import speech_recognition as sr
import pyaudio
from flask import Flask, jsonify, request, url_for
from werkzeug.utils import redirect
import csv


engine = pyttsx3.init()
app = Flask(__name__)

example_json = {
  "links": {
    "self": "http://example.com/articles",
    "next": "http://example.com/articles?page[offset]=2",
    "last": "http://example.com/articles?page[offset]=10"
  },
  "data": [{
    "type": "articles",
    "id": "1",
    "attributes": {
      "title": "JSON:API paints my bikeshed!"
    },
    "relationships": {
      "author": {
        "links": {
          "self": "http://example.com/articles/1/relationships/author",
          "related": "http://example.com/articles/1/author"
        },
        "data": { "type": "people", "id": "9" }
      },
      "comments": {
        "links": {
          "self": "http://example.com/articles/1/relationships/comments",
          "related": "http://example.com/articles/1/comments"
        },
        "data": [
          { "type": "comments", "id": "5" },
          { "type": "comments", "id": "12" }
        ]
      }
    },
    "links": {
      "self": "http://example.com/articles/1"
    }
  }],
  "included": [{
    "type": "people",
    "id": "9",
    "attributes": {
      "firstName": "Dan",
      "lastName": "Gebhardt",
      "twitter": "dgeb"
    },
    "links": {
      "self": "http://example.com/people/9"
    }
  }, {
    "type": "comments",
    "id": "5",
    "attributes": {
      "body": "First!"
    },
    "relationships": {
      "author": {
        "data": { "type": "people", "id": "2" }
      }
    },
    "links": {
      "self": "http://example.com/comments/5"
    }
  }, {
    "type": "comments",
    "id": "12",
    "attributes": {
      "body": "I like XML better"
    },
    "relationships": {
      "author": {
        "data": { "type": "people", "id": "9" }
      }
    },
    "links": {
      "self": "http://example.com/comments/12"
    }
  }]
}
data_json = dict()
reader = csv.DictReader(open('data.csv'))
for row in reader:
    data_json.update(row)

@app.route('/')
def index():
    return "Welcome to our app"

@app.route('/takeorder', methods = ['POST'])
def post():
    if request.method == 'POST':
        #data = request.form[example_json]
        return jsonify(data_json)



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
    app.run(debug=True)
    pass