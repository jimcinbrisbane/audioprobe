import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
RED_PIN = 21
YELLOW_PIN = 20
GREEN_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

def perform_function():
    try:
        # Example: Indicate the function is performing
        print("Function is performing...")

        # Turn on the red LED
        GPIO.output(RED_PIN, GPIO.HIGH)
        time.sleep(2)  # Simulate the function taking time
        
        # Turn off the red LED
        GPIO.output(RED_PIN, GPIO.LOW)

        # Indicate yellow for intermediate state
        GPIO.output(YELLOW_PIN, GPIO.HIGH)
        time.sleep(2)  # Simulate another part of the function
        GPIO.output(YELLOW_PIN, GPIO.LOW)

        # Indicate green for completion
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(GREEN_PIN, GPIO.LOW)

        print("Function completed.")
    
    finally:
        # Clean up GPIO settings
        GPIO.cleanup()

if __name__ == "__main__":
    perform_function()
