import RPi.GPIO as GPIO
import time
import sounddevice as sd
from scipy.io.wavfile import write

# Define the GPIO pins
touch_pin_record = 27
touch_pin_play = 23

# Set up the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(touch_pin_record, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(touch_pin_play, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
    # Sampling frequency
    freq = 44100

    print("Recording started...")
    
    # Start recorder with the given values of duration and sample frequency
    recording = []

    # Record audio while the button is pressed
    while GPIO.input(touch_pin_record) == GPIO.LOW:
        frame = sd.rec(1, samplerate=freq, channels=2, dtype='int16')
        sd.wait()
        recording.append(frame)
    

    
    # Save the recording to a file
    write("recording1.wav", freq, recording)
    print("Recording stopped and saved to recording1.wav")

try:
    while True:
        if GPIO.input(touch_pin_record) == GPIO.LOW:
          print("Recording")
          record()
            
        if GPIO.input(touch_pin_play) == GPIO.LOW:
          print("Play")
          play()
        time.sleep(0.1)  # Small delay to debounce button presses

except KeyboardInterrupt:
    print("Program terminated.")

finally:
    GPIO.cleanup()
