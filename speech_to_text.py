import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# open the microphone and start recording
with sr.Microphone() as source:
    print("Speak now!")
    audio = r.listen(source)

try:
    # recognize speech using Google Speech Recognition
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand your speech")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
