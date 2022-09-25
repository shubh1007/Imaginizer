import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("Listening...")
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    
    text = r.recognize_google(audio_data)
    print(f"Text Detected: {list(map(str, text.split()))}")