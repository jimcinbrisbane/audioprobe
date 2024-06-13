#record wav
#pip install wavio
#pip install scipy
#pip install sounddevice
#first if pi
#sudo apt-get install libportaudio2
#probe0@raspberrypi:~/audioprobe $ python -m venv env
# source env/bin/activate 
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

def record():
    
    # Sampling frequency
    freq = 50000

    # Recording duration
    duration = 10
    print("start now for 10s")

    # Start recorder with the given values of 
    # duration and sample frequency
    recording = sd.rec(int(duration * freq), 
                    samplerate=freq, channels=2)
    # Record audio for the given number of seconds
    sd.wait()
    write("recording1.wav", freq, recording)

    #wv.write("recording1.wav", recording, freq, sampwidth=2)

record()
