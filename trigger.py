import sounddevice as sd
import numpy as np
import RPi.GPIO as GPIO
import time
import wave

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(27, GPIO.IN)

# Audio recording settings
samplerate = 44100  # Sample rate
channels = 2       # Stereo recording
duration = 10      # Duration of the recording in seconds

# Buffer to store audio data
audio_buffer = []

# Callback function to save audio
def save_audio(audio_data, filename="recording1.wav"):
    # Convert the audio buffer to numpy array
    audio_data = np.concatenate(audio_data, axis=0)

    # Save the audio data to a WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(samplerate)
        wf.writeframes(audio_data.tobytes())

# Function to record audio
def record_audio():
    print("Recording started...")
    audio_buffer.clear()
    start_time = time.time()
    
    def callback(indata, frames, time, status):
        if status:
            print(status)
        audio_buffer.append(indata.copy())

        # Check if the recording duration has been reached
        if time.time() - start_time > duration:
            sd.stop()

    # Start recording
    with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback):
        sd.sleep(duration * 1000)
    print("Recording stopped.")

# Callback function to handle GPIO trigger
def gpio_callback(channel):
    print("GPIO23 triggered! Saving audio...")
    save_audio(audio_buffer)

# Add event detection on GPIO23
GPIO.add_event_detect(23, GPIO.RISING, callback=gpio_callback, bouncetime=300)
GPIO.add_event_detect(27, GPIO.RISING, callback=gpio_callback, bouncetime=300)

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




try:
    while True:
        # Check if pressure is detected
        if GPIO.input(27) == GPIO.HIGH:
          print("record")
          record_audio()
        if GPIO.input(23) == GPIO.HIGH:
          save_audio()
          print("play")
          play()
        
        # Delay to prevent CPU hogging
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO settings
    GPIO.cleanup()