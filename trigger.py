import RPi.GPIO as GPIO
import time
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import pygame

# Constants
RECORD_PIN = 27
PLAY_PIN = 23
SAMPLE_RATE = 48000
FRAME_DURATION = 1  # in seconds
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

        while GPIO.input(PLAY_PIN) != GPIO.HIGH:
            frame = sd.rec(FRAME_SIZE, samplerate=SAMPLE_RATE, channels=2)
            sd.wait()
            recording.append(frame)

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

try:
    while True:
        if GPIO.input(RECORD_PIN) == GPIO.HIGH:
            print("Recording button pressed")
            record()
        elif GPIO.input(PLAY_PIN) == GPIO.HIGH:
            print("Playback button pressed")
            play()

        # Delay to prevent CPU hogging
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO settings
    GPIO.cleanup()
    print("Program terminated and GPIO cleaned up.")
