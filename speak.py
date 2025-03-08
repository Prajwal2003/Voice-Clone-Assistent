import pyttsx3  

def speak(text):  
    engine = pyttsx3.init()  
    engine.say(text)  
    engine.runAndWait()  

if __name__ == "__main__":  
    while True:  
        text = input("Enter text to speak (or 'exit' to quit): ")  
        if text.lower() == 'exit':  
            break  
        speak(text)  
