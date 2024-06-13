import RPi.GPIO as GPIO
import time
import sounddevice as sd
from scipy.io.wavfile import write

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
    while GPIO.input(27) == GPIO.HIGH:
        frame = sd.rec(1, samplerate=freq, channels=2, dtype='int16')
        sd.wait()
        recording.append(frame)
    

    
    # Save the recording to a file
    write("recording1.wav", freq, recording)
    print("Recording stopped and saved to recording1.wav")




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
        if GPIO.input(23) == GPIO.HIGH:
          print("record")
          record()
        if GPIO.input(27) == GPIO.HIGH:
          print("play")
          play()
        
        # Delay to prevent CPU hogging
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO settings
    GPIO.cleanup()