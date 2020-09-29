import webbrowser as wb
import  speech_recognition as sr
import pyttsx3
import os


pyttsx3.speak("Hello Gulsha I am your assistant Joy How can i help you?")
print("--------------Welcome to my world-----------------")

while True:
  print()
  print("\t \t Tell me your requirement... i am listening : ", end='')
  r= sr.Recognizer()
  with sr.Microphone() as source:
    pyttsx3.speak("Start Talking...")
    audio= r.listen(source)
    print("Speech Done")
  Choice= r.recognize_google(audio)
  if(("tell" in Choice) or ("about" in Choice) and ("yourself" in Choice)):
    pyttsx3.speak("I am your voice assistant Joy and i can run linux and GUI programs for you")
  elif "date" in Choice:
    wb.open("http://192.168.43.211/cgi-bin/menu.py?x=date&y=date&Submit=Submit")
  elif (("cal" in Choice) or ("calendar" in Choice)):
    wb.open("http://192.168.43.211/cgi-bin/menu.py?x=cal&y=cal&Submit=Submit")
  elif "storage" in Choice:
    wb.open("http://192.168.43.211/cgi-bin/menu.py?x=df+-h&y=df+-h&Submit=Submit")
  elif (("IP" in Choice) or ("ifconfig" in Choice)):
    wb.open("http://192.168.43.211/cgi-bin/menu.py?x=ifconfig&y=ifconfig&Submit=Submit")
  elif (("status" in Choice) or ("docker" in Choice)):
    wb.open("http://192.168.43.211/cgi-bin/menu.py?x=systemctl+status+docker&y=systemctl+status+docker&Submit=Submit")
  elif "who" in Choice or "am" in Choice:
    wb.open("http://192.168.43.211/cgi-bin/menu.py?x=whoami&y=whoami&Submit=Submit")
  elif "port" in Choice :
    wb.open("http://192.168.43.211/cgi-bin/menu.py?x=netstat+-tnlp&y=netstat+-tnlp&Submit=Submit")
  elif "hadoop" in Choice:
    wb.open("http://192.168.43.211/cgi-bin/menu.py?x=hadoop+version&y=hadoop+version&Submit=Submit")
  elif "java" in Choice:
    wb.open("http://192.168.43.211/cgi-bin/menu.py?x=java+-version&y=java+--version&Submit=Submit")
  elif (("notepad" in Choice) or ("text editor" in Choice)):
    pyttsx3.speak("Opening Editor,Please Wait..")
    os.system("notepad")
  elif (("paint" in Choice) or ("draw" in Choice )):
    pyttsx3.speak("Opening Paint,Please Wait..")
    os.system("mspaint")
  elif (("ok" in Choice) or ("bye" in Choice)):
    break
  else:
    pyttsx3.speak("I didn't get you..Gulsha?")

pyttsx3.speak("Task Completed...Thankyou...Bye Bye..Good Day!!")
print("Task Completed...Thankyou...Bye Bye..Good Day!!")