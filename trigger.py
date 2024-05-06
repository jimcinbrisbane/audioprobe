#link function to pin trigger buttons
# pinx = record on hold
# piny = flash on new msg
# pinz = press to play msg

#maybe install pi os lite if run headless apps
#sudo apt update -y && sudo apt upgrade -y
import time
import RPi.GPIO as GPIO
touch_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(touch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def touch_det(pin):
    touch=GPIO.input(pin)
    return touch

try:
    while True:
        if touch_det(touch_pin): print('['+time.ctime()+'] - '+'Touch Detected')
        time.sleep(0.2) # sleep 0.2s, but we want to play audio on 17

except KeyboardInterrupt:
  print('interrupted!')
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

  