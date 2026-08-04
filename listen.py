import sounddevice as sd
import speech_recognition as sr
import tempfile
import os
import wave

def listen():
    r = sr.Recognizer()

    fs = 16000        # Sample rate
    duration = 5      # seconds

    print("Listening...")

    try:
        recording = sd.rec(
            int(duration * fs),
            samplerate=fs,
            channels=1,
            dtype='int16'
        )
        sd.wait()

        # Create temp file path (not opened)
        temp_path = tempfile.mktemp(suffix=".wav")

        # Write proper PCM WAV
        with wave.open(temp_path, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(fs)
            wf.writeframes(recording.tobytes())

        # Read audio
        with sr.AudioFile(temp_path) as source:
            audio = r.record(source)

        os.remove(temp_path)

        text = r.recognize_google(audio).lower()
        print("You:", text)
        return text

    except Exception as e:
        print("Listening error:", e)
        return "none"
