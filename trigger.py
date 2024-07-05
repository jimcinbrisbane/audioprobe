import RPi.GPIO as GPIO
import time
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import pygame
from send import upload_blob 
from getfile import download_blob


# Constants
STOP = 18
RECORD_PIN = 27
PLAY_PIN = 23
SAMPLE_RATE = 48000
FRAME_DURATION = 2  # in seconds
FRAME_SIZE = SAMPLE_RATE * FRAME_DURATION

def play():
    try:
        print("Playback started...")
        pygame.mixer.init()
        pygame.mixer.music.load('./recording1.wav')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        print("Playback finished.")
    except Exception as e:
        print(f"An error occurred during playback: {e}")

def record():
    try:
        print("Recording started...")
        recording = []

        # Record until the STOP button is pressed
        while GPIO.input(STOP) != GPIO.HIGH:
            frame = sd.rec(FRAME_SIZE, samplerate=SAMPLE_RATE, channels=2)
            sd.wait()  # Wait until the frame is recorded
            recording.append(frame)

        # Concatenate all recorded frames into a single array
        if recording:
            recording = np.concatenate(recording, axis=0)
            write("recording1.wav", SAMPLE_RATE, recording)
            print("Recording stopped and saved to recording1.wav")
        else:
            print("No recording made.")
    except Exception as e:
        print(f"An error occurred during recording: {e}")
# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the pin as input
GPIO.setup(RECORD_PIN, GPIO.IN)
GPIO.setup(PLAY_PIN, GPIO.IN)
GPIO.setup(STOP, GPIO.IN)
import datetime
import pymongo
myclient = pymongo.MongoClient("mongodb+srv://probe0:probe0@audioprobe.yoroiqf.mongodb.net/?retryWrites=true&w=majority&appName=audioprobe")

mydb = myclient["audioprobe"]
mycol = mydb["audioprobe"]
old_file_name = " "

import requests

def download_wav_file(filename):
    print(filename)
    download_blob("audioprobe", "2024-06-16 00:44:57.143665", "download.wav")    
    pygame.mixer.init()
    pygame.mixer.music.load('./download.wav')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue





try:
    while True:
        if GPIO.input(RECORD_PIN) == GPIO.HIGH:
            print("Recording button pressed")
            record()
            filename = str(datetime.datetime.now())
            mydict = { 
                "probe": "probe0", 
                "file_name": f"https://storage.cloud.google.com/audioprobe/{filename}.wav",
                'datetime_field': filename 
            }
            x = mycol.insert_one(mydict)
            upload_blob("audioprobe", './recording1.wav', filename)
        elif GPIO.input(PLAY_PIN) == GPIO.HIGH:
            recent_entry = mycol.find_one(
                {"probe": "probe0"},  # Query to match documents with "probe": "probe0"
                sort=[("datetime_field", -1)]  # Sort by the datetime field in descending order
            )

            # Extract the file name from the recent entry
            datetime_field = recent_entry['datetime_field'] if recent_entry else None
            if old_file_name is not datetime_field:
                filename = datetime_field + ".wav"
                download_wav_file(filename)
                old_file_name = datetime_field
            else:
                pygame.mixer.init()
                pygame.mixer.music.load('./download.wav')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
            
        elif GPIO.input(STOP) == GPIO.HIGH:
            print("Audio play back, this is what you sent")
            play()
        # Delay to prevent CPU hogging
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO settings
    GPIO.cleanup()
    print("Program terminated and GPIO cleaned up.")

