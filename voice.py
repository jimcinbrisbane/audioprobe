import sounddevice as sd
import numpy as np
import speech_recognition as sr
import wave
import time
import os
import pygame

# Set file path for audio message
AUDIO_FILE_PATH = "message.wav"
RECORD_DURATION = 10  # Seconds of audio to record

# Function to record audio when triggered
def record_audio(filename, duration):
    # Use sounddevice to record
    sample_rate = 44100
    print(f"Recording for {duration} seconds...")
    
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    
    # Save the recording to a file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    wf.writeframes(recording.tobytes())
    wf.close()
    print(f"Audio saved to {filename}")

# Function to listen for the "record" command
def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Listening for the 'record' command...")
    
    while True:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized command: {command}")
            
            # Trigger action if "record" command is spoken
            if "machine" or "send" and "cassandra" in command:
                print("Record command detected.")
                return True  # Trigger recording

        except sr.UnknownValueError:
            print("doing nothing")
        except sr.RequestError as e:
            print(f"Error with Google Speech Recognition service: {e}")

# Main function
if __name__ == "__main__":
    pygame.mixer.init()
    while True:
        if listen_for_command():
            pygame.mixer.music.load('./cas.wav')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
                # Start recording audio when 'record' command is detected
            record_audio(AUDIO_FILE_PATH, RECORD_DURATION)
                # Once recorded, you can add functionality to send the audio file
                # e.g., send_to_server(AUDIO_FILE_PATH)

            pygame.mixer.music.load('./playback.wav')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            pygame.mixer.music.load('./message.wav')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            pygame.mixer.music.load('./sent.wav')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
        time.sleep(1)  # Pause before next loop iteration
