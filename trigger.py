import RPi.GPIO as GPIO
import time
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

#play audio
#update pip
#pip3 install pygame
import pygame

def play():
    print("Playback started...")
    pygame.mixer.init()
    pygame.mixer.music.load('./recording1.wav')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    print("Playback finished.")

def record():
    freq = 48000

    print("Recording started...")
    
    # Record audio while the button is pressed
    recording = []
    while GPIO.input(23) != GPIO.HIGH:
        frame = sd.rec(50000, samplerate=freq, channels=2)
        sd.wait()
        recording.append(frame)
    if recording:
          # Convert list to numpy array
          recording = np.concatenate(recording, axis=0)
          
          # Save the recording to a file
          write("recording1.wav", 44100, recording)
          print("Recording stopped and saved to recording1.wav")
    else:
          print("No recording made.")
    



import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the pin number

# Set the pin as input
GPIO.setup(23, GPIO.IN)
GPIO.setup(27, GPIO.IN)

try:
    while True:
        # Check if pressure is detected
        if GPIO.input(27) == GPIO.HIGH:
          print("record")
          record()
        if GPIO.input(23) == GPIO.HIGH:
          print("play")
          play()
        
        # Delay to prevent CPU hogging
        time.sleep(0.25)

except KeyboardInterrupt:
    # Clean up GPIO settings
    GPIO.cleanup()