from listen import listen
from speak import speak
from commands import process_command

WAKE_WORDS = ["hey jarvis", "jarvis"]

def has_wake_word(text):
    for word in WAKE_WORDS:
        if word in text:
            return True
    return False


if __name__ == "__main__":
    speak("Hello! Say 'Hey Jarvis' to wake me up.")

    while True:
        print("\nWaiting for wake word...")
        text = listen()

        if text == "none":
            continue

        if has_wake_word(text):
            speak("I'm listening...")
            command = listen()

            if command != "none":
                process_command(command)
