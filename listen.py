import speech_recognition as sr

def voice_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("🎤 Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print("📝 You said:", text)
        except sr.UnknownValueError:
            print("❌ Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("❌ Could not request results, check your internet connection.")

if __name__ == "__main__":
    while(True):
        voice_to_text()
