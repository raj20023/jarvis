import pyttsx3

# initialize the pyttsx3 engine
engine = pyttsx3.init()

# set properties for the speech
engine.setProperty('rate', 150)  # set the speaking rate in words per minute
engine.setProperty('volume', 1)  # set the volume level (0-1)

# get input text from the user
text = input('Enter the text you want to convert to speech: ')

# convert the text to speech
engine.say(text)
engine.runAndWait()
