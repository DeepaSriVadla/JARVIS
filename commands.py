from speak import speak
import os
import webbrowser
import datetime
import wikipedia

def process_command(command):
    command = command.lower().strip()

    # -------- OPEN APPS --------
    if "open notepad" in command:
        speak("Opening Notepad")
        os.system("start notepad")

    elif "open chrome" in command or "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("start calc")

    # -------- WIKIPEDIA --------
    elif "wikipedia" in command:
        speak("Searching Wikipedia")
        try:
            command = command.replace("wikipedia", "")
            result = wikipedia.summary(command, sentences=2)
            speak(result)
            print(result)
        except Exception as e:
            speak("Sorry, I could not find information")
            print(e)

    # -------- MUSIC --------
    elif "play music" in command:
        try:
            music_folder = r"C:\Users\Public\Music"  # change if needed
            songs = os.listdir(music_folder)
            if songs:
                os.startfile(os.path.join(music_folder, songs[0]))
                speak("Playing music")
            else:
                speak("No songs found")
        except Exception as e:
            speak("Music folder not found")
            print(e)

    # -------- TIME --------
    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time_now}")

    # -------- EXIT --------
    elif "stop jarvis" in command or "exit" in command:
        speak("Goodbye")
        exit()

    else:
        speak("I did not understand the command")