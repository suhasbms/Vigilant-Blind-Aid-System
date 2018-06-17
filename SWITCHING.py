import RPi.GPIO as GPIO
import time
import os
from subprocess import call

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(3,GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(2,GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "WELCOME TO VIGILANT BLIND AID SYSTEM"
os.system('echo "WELCOME TO VIGILANT BLIND AID SYSTEM" | festival --tts')

GPIO.setwarnings(False)

while GPIO.input(2) == False:
  
  if GPIO.input(3) == False:
    
    os.system("sudo rm tts.txt")
    os.system("sudo rm test.jpg")
    os.system("clear")
    os.system("sudo python ./lost.py")
    

  else:

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    os.system("clear")
    os.system("sudo bash ./tts.sh")
  
print "good BYE"
os.system('echo "good BYE" | festival --tts')
GPIO.cleanup()
os.system("clear")
