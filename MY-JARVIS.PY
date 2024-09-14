import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer= sr.Recognizer()
engine= pyttsx3.init()
newsapi=   "5ef6b780f069415fae1e0dd6b42a4719"

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
    # print(c)

    if "open youtube" in c.lower():
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com/")
    elif"open instagram" in c.lower():
        print("Opening Instagram...")
        webbrowser.open("https://www.instagram.com/") 
    elif"open google" in c.lower():
        print("Opening Google...")
        webbrowser.open("https://www.google.com/")
    elif"open spotify" in c.lower():
        print("Opening Spotify...")
        webbrowser.open("https://www.spotify.com")
    elif"open linkedin" in c.lower():
        print("Opening linkedin....")
        webbrowser.open("https://www.linkedin.com/")
    elif"open facebook" in c.lower():
        print("opening facebook")
        webbrowser.open("https://www.facebook.com/")
    elif"open twitter" in c.lower():
        print("Opening Twitter....")
        webbrowser.open("https://www.twitter.com")
    elif"open emails" in c.lower():
        print("Opening emails....")
        webbrowser.open("https://www.mail.google.com")

    elif c.lower().startswith("play"):
        song= c.lower().split(" ",)[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif c.lower().startswith("news"):
        try:   
            # Make API request to fetch news headlines
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])
                if articles:
                    for i, article in enumerate(articles, 1):
                        speak(f"Headline {i}: {article['title']}")
                        # below some else lines are optional
                else:
                    speak("No news articles available.")
            else:
                speak("Failed to retrieve news.")
        except Exception as e:
            speak(f"An error occurred while fetching news: {e}")
       
    
    else:
        speak("sorry,I didn't understand that command")
        print("Unknown command")
    
    
if __name__ == "__main__":

    speak("Jarvis  is  ready   tell  me  what  can  i  do  for  you  ayush")
    while True:
        r=sr.Recognizer()
        print("recognizing....")
        try:
            with sr.Microphone() as sourse:
                print("listning...")
                audio= r.listen(sourse,timeout=5,phrase_time_limit=3)
                word=r.recognize_google(audio)
                if word.lower()=="jarvis" or word.lower()=="good jarvis":
                 speak("Yes Ayush")
                 speak(" It's  my  pleasure")
                # lsiten for commands
                with sr.Microphone() as sourse:
                    print("Jarvis Active...")
                    audio= r.listen(sourse,timeout=5,phrase_time_limit=5)
                    command=r.recognize_google(audio)

                    processcommand(command)
        except sr.UnknownValueError:
            print("Sorry i didn't catch that.")
            speak("Sorry i didn't catch that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("Sorry, I am unable to connect to the speech service.")
        except Exception as e:
            print(f"Error: {e}")