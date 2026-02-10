import speech_recognition as sr
import pyttsx3
import datetime

# ---------- SPEAK FUNCTION (FIXED) ----------
def speak(text):
    engine = pyttsx3.init('sapi5')   # RE-INIT EVERY TIME (KEY FIX)
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ---------- LISTEN FUNCTION ----------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        print("Could not understand")
        return ""

# ---------- MAIN ----------
print("Voice assistant started")
speak("Voice assistant started. How can I help you?")

while True:
    command = listen()

    if command == "":
        continue

    if "hello" in command:
        print("Replying: Hello")
        speak("Hello! Nice to hear you")

    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        print("Replying time")
        speak(f"The time is {time_now}")

    elif "exit" in command or "quit" in command:
        print("Exiting")
        speak("Goodbye. Have a nice day")
        break
