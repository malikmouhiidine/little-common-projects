import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import pyjokes


print('Loading your AI personal assistant - M-ice')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Bonjour malik")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("bon après-midi")
        print("Hello,Good Afternoon")
    else:
        speak("Bonsoir")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said: {statement}\n")

        except Exception as e:
            speak("Pardonnez-moi, s'il vous plaît dites-le encore")
            return "None"
        return statement

speak("Bonjour Malik")
wishMe()


if __name__=='__main__':


    while True:
        speak("Dites-moi comment puis-je vous aider maintenant?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak("votre assistant personnel carrot s'arrête, au revoir")
            print('your personal assistant M-ice is shutting down,Good bye')
            break

# Here u could just add as many options as u want

        if 'wikipedia' in statement:
            speak('Recherche sur Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("Selon Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube est ouvert maintenant")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome est maintenant ouvert")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail est maintenant ouvert")
            time.sleep(5)

        elif "weather" in statement:
            api_key=os.environ.get('API_KEY_WEATHER')
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("quel est le nom de la ville")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" La température en unité kelvin est " +
                      str(current_temperature) +
                      "\n l'humidité en pourcentage est " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" La température en unité kelvin est = " +
                      str(current_temperature) +
                      "\n l'humidité en pourcentage est = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" Ville introuvable ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Le temps est {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak("Je suis M-ice version 1 point O votre assistant personnel. Je suis programmé pour des tâches mineures comme "
                  "ouvrir youtube, google chrome, gmail et stackoverflow, prévoir l'heure, prendre une photo, rechercher wikipedia, prévoir la météo"
                  "dans différentes villes, obtenez les principales nouvelles de l'époque de l'Inde et vous pouvez aussi me poser des questions informatiques ou géographiques!")

        elif "who build you" in statement  or "who discovered you" in statement:
            speak("J'ai été construit par Malik")
            print("I was built by Malik")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Voici stackoverflow")
        elif 'joke' in statement:
            speak(pyjokes.get_joke())
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.aljazeera.net/")
            speak("Voici quelques titres de l'aljazeera, Bonne lecture")
            time.sleep(6)
        elif 'read something' in statement:
            news = webbrowser.open_new_tab("https://www.reddit.com/r/programming/")
            speak('Voici quelques titres de reddit pour les développeurs, Bonne lecture')
            time.sleep(6)

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('Je peux répondre aux questions informatiques et géographiques et quelle question voulez-vous poser maintenant')
            question=takeCommand()
            app_id=os.environ.get("API_KEY_ALPHA")
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement:
            speak("Ok, votre PC se déconnectera dans 10 secondes, assurez-vous de quitter toutes les applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)