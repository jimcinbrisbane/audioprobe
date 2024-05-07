import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the pin number
pin = 23

# Set the pin as input
GPIO.setup(pin, GPIO.IN)

try:
    while True:
        # Check if pressure is detected
        if GPIO.input(pin) == GPIO.HIGH:
            print("Pressure detected")
        
        # Delay to prevent CPU hogging
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO settings
    GPIO.cleanup()
  #establish domain
  #loss of connection, eg retire, impact... ref case study, the importance
  #establish/reestablish connection
  #ambianint social iot
  #how is the solution going to help
  #aim needs to be bigger,"will xxx xxx"overall and objectives is details, smart goals
  # what is in scope, refine prototype, insight within the brisbane region
  # methdology mix method, qualititive human centered design, method: interview, tam, sus, obsevation, technology probe
#people invloved, graph need to show iterative appoach
#need timeline,highlight milestone 
#make a graph for how the technology probe works.
#image source, photogapher name,link

  
  #establish domain
  #loss of connection, eg retire, impact... ref case study, the importance
  #establish/reestablish connection
  #ambianint social iot
  #how is the solution going to help
  #aim needs to be bigger,"will xxx xxx"overall and objectives is details, smart goals
  # what is in scope, refine prototype, insight within the brisbane region
  # methdology mix method, qualititive human centered design, method: interview, tam, sus, obsevation, technology probe
#people invloved, graph need to show iterative appoach
#need timeline,highlight milestone 
#make a graph for how the technology probe works.
#image source, photogapher name,link

  
