#record wav
#pip install wavio
#pip install scipy
#pip install sounddevice
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
freq = 44100

# Recording duration
duration = 25
print("start now 25s")

# Start recorder with the given values of 
# duration and sample frequency
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)
# Record audio for the given number of seconds
sd.wait()

wv.write("recording1.wav", recording, freq, sampwidth=2)
