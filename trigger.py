import RPi.GPIO as GPIO
import time
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import pygame
from send import upload_blob 

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



import time

import paho.mqtt.client as paho
from paho import mqtt


# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    """
        Prints the result of the connection with a reasoncode to stdout ( used as callback for connect )

        :param client: the client itself
        :param userdata: userdata is set when initiating the client, here it is userdata=None
        :param flags: these are response flags sent by the broker
        :param rc: stands for reasonCode, which is a code for the connection result
        :param properties: can be used in MQTTv5, but is optional
    """
    print("CONNACK received with code %s." % rc)


# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    """
        Prints mid to stdout to reassure a successful publish ( used as callback for publish )

        :param client: the client itself
        :param userdata: userdata is set when initiating the client, here it is userdata=None
        :param mid: variable returned from the corresponding publish() call, to allow outgoing messages to be tracked
        :param properties: can be used in MQTTv5, but is optional
    """
    print("mid: " + str(mid))


# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    """
        Prints a reassurance for successfully subscribing

        :param client: the client itself
        :param userdata: userdata is set when initiating the client, here it is userdata=None
        :param mid: variable returned from the corresponding publish() call, to allow outgoing messages to be tracked
        :param granted_qos: this is the qos that you declare when subscribing, use the same one for publishing
        :param properties: can be used in MQTTv5, but is optional
    """
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    """
        Prints a mqtt message to stdout ( used as callback for subscribe )

        :param client: the client itself
        :param userdata: userdata is set when initiating the client, here it is userdata=None
        :param msg: the message with topic and payload
    """
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="probe", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("hivemq.webclient.1718857186246", "2Q*o.yCXe3Hh8,kuB!5D")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("feeb635cdc89485984fe56b53425bd47.s1.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("/", qos=1)

# a single publish, this can also be done in loops, etc.

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop

try:
    while True:
        client.loop_forever()
        if GPIO.input(RECORD_PIN) == GPIO.HIGH:
            print("Recording button pressed")
            record()
            filename = str(datetime.datetime.now())+".wav"
            client.publish("/", payload=filename, qos=1)
            upload_blob("audioprobe", './recording1.wav', filename)
        elif GPIO.input(PLAY_PIN) == GPIO.HIGH:
            print("Incoming msg")
            play()
        elif GPIO.input(STOP) == GPIO.HIGH:
            print("Audio play back, this is what you sent")
            play()
        # Delay to prevent CPU hogging
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO settings
    GPIO.cleanup()
    print("Program terminated and GPIO cleaned up.")