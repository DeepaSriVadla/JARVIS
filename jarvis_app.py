import tkinter as tk
import threading
from speak import speak
from listen import listen
from commands import process_command

WAKE_WORDS = ["hey jarvis", "hello jarvis", "jarvis"]
listening = False

def set_mic(state):
    if state:
        mic_label.config(text="🎙️ Listening", fg="green")
    else:
        mic_label.config(text="🔴 Not Listening", fg="red")

def jarvis_loop():
    global listening
    speak("Jarvis activated")

    while listening:
        status.config(text="Listening for wake word...")
        text = listen()

        if not listening:
            break

        if text == "none":
            continue

        if any(w in text for w in WAKE_WORDS):
            speak("Yes")
            status.config(text="Listening to command...")

            command = listen()
            if command != "none":
                status.config(text="Processing...")
                process_command(command)
                status.config(text="Listening...")

    set_mic(False)
    status.config(text="Stopped")

def start_listening():
    global listening
    if listening:
        return
    listening = True
    set_mic(True)
    threading.Thread(target=jarvis_loop, daemon=True).start()

def stop_listening():
    global listening
    listening = False
    set_mic(False)
    speak("Jarvis stopped")

# ---------------- UI ----------------
window = tk.Tk()
window.title("Jarvis Desktop Assistant")
window.geometry("380x300")
window.resizable(False, False)

title = tk.Label(window, text="JARVIS", font=("Arial", 22, "bold"))
title.pack(pady=15)

mic_label = tk.Label(window, text="🔴 Not Listening", font=("Arial", 12))
mic_label.pack(pady=5)

btn_start = tk.Button(
    window,
    text="🎙 Ask Jarvis (Start)",
    font=("Arial", 13),
    width=22,
    command=start_listening
)
btn_start.pack(pady=10)

btn_stop = tk.Button(
    window,
    text="⏹ Stop Listening",
    font=("Arial", 12),
    width=22,
    command=stop_listening
)
btn_stop.pack(pady=5)

status = tk.Label(window, text="Idle", font=("Arial", 10))
status.pack(pady=15)

window.mainloop()
