import pyttsx3

def speak(text):
    print("Assistant:", text)
    
    engine = pyttsx3.init()

    # --- FIX: choose working voice engine for Windows ---
    engine.setProperty('rate', 180)   # speech speed
    voices = engine.getProperty('voices')
    
    # try different voices (0, 1, 2,...)
    try:
        engine.setProperty('voice', voices[1].id)  # male voice usually index 1
    except:
        engine.setProperty('voice', voices[0].id)  # fallback
        
    engine.say(text)
    engine.runAndWait()
