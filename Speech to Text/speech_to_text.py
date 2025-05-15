import speech_recognition as sr

# Create a recognizer
recognizer = sr.Recognizer()

# Use your microphone
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)

    try:
        # Use Google to recognize the speech
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except:
        print("Sorry, could not recognize your voice.")
