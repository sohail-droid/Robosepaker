import pyttsx3
engine = pyttsx3.init('sapi5')
print("Welcome to Robot speaker 3.0 Created by Sohail")
engine.say("Welcome to Robot speaker 3.0 Created by Sohail")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    list = ["hii","hello","how are you"]
    while (1):
        x = input("\nEnter text to Talk :")
        for i in list:
            if x == i in list:
                speak("hii sir have a great day")
                print("hii sir have a great day")



        command = print(f"Assistant:  {x}")
        if x == "exit":
            speak("Turning off")
            speak(x)
            break
        speak(x)



