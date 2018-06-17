import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
TRIG1 = 17
TRIG2 = 27
TRIG3 = 22
TRIG4 = 10
TRIG5 = 9
ECHO1 = 5
ECHO2 = 6
ECHO3 = 13
ECHO4 = 19
ECHO5 = 26
VOUT1 = 20
VOUT2 = 21

GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(TRIG4,GPIO.OUT)
GPIO.setup(TRIG5,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(ECHO3,GPIO.IN)
GPIO.setup(ECHO4,GPIO.IN)
GPIO.setup(ECHO5,GPIO.IN)
GPIO.setup(VOUT1,GPIO.IN)
GPIO.setup(VOUT2,GPIO.IN)

while True:

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(TRIG1, GPIO.OUT)
	GPIO.setup(ECHO1, GPIO.IN)
	GPIO.output(TRIG1, False)
	time.sleep(0.05)
	GPIO.output(TRIG1, True)
	time.sleep(0.00001)
	GPIO.output(TRIG1, False)
	while GPIO.input(ECHO1) == 0:
		pulse_start1 = time.time()
	while GPIO.input(ECHO1) == 1:
		pulse_end1 = time.time()
	pulse_duration1 = pulse_end1 - pulse_start1
	distance1 = pulse_duration1 * 17150
	distance1 = round(distance1, 2)
	if distance1 < 30:
		mode = GPIO.getmode()
		print " mode =" + str(mode)
		GPIO.cleanup()
		StepPinForward = 8
		StepPinBackward = 26
		sleeptime = 1
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(StepPinForward, GPIO.OUT)
		GPIO.setup(StepPinBackward, GPIO.OUT)
		def forward(x):
			GPIO.output(StepPinForward, GPIO.HIGH)
			print "forwarding running  motor1 "
			time.sleep(x)
			GPIO.output(StepPinForward, GPIO.LOW)
		forward(1)
		GPIO.cleanup()

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(TRIG2, GPIO.OUT)
	GPIO.setup(ECHO2, GPIO.IN)
	GPIO.output(TRIG2, False)
	time.sleep(0.05)
	GPIO.output(TRIG2, True)
	time.sleep(0.00001)
	GPIO.output(TRIG2, False)
	while GPIO.input(ECHO2) == 0:
		pulse_start2 = time.time()
	while GPIO.input(ECHO2) == 1:
		pulse_end2 = time.time()
	pulse_duration2 = pulse_end2 - pulse_start2
	distance2 = pulse_duration2 * 17150
	distance2 = round(distance2, 2)
	if distance2 < 30:
		mode = GPIO.getmode()
		print " mode =" + str(mode)
		GPIO.cleanup()
		StepPinForward = 10
		StepPinBackward = 26
		sleeptime = 1
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(StepPinForward, GPIO.OUT)
		GPIO.setup(StepPinBackward, GPIO.OUT)
		def forward(x):
			GPIO.output(StepPinForward, GPIO.HIGH)
			print "forwarding running  motor1 "
			time.sleep(x)
			GPIO.output(StepPinForward, GPIO.LOW)
		forward(1)
		GPIO.cleanup()

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(TRIG3, GPIO.OUT)
	GPIO.setup(ECHO3, GPIO.IN)
	GPIO.output(TRIG3, False)
	time.sleep(0.05)
	GPIO.output(TRIG3, True)
	time.sleep(0.00001)
	GPIO.output(TRIG3, False)
	while GPIO.input(ECHO3) == 0:
		pulse_start3 = time.time()
	while GPIO.input(ECHO3) == 1:
		pulse_end3 = time.time()
	pulse_duration3 = pulse_end3 - pulse_start3
	distance3 = pulse_duration3 * 17150
	distance3 = round(distance3, 2)
	if distance3 < 30:
		mode = GPIO.getmode()
		print " mode =" + str(mode)
		GPIO.cleanup()
		StepPinForward = 12
		StepPinBackward = 26
		sleeptime = 1
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(StepPinForward, GPIO.OUT)
		GPIO.setup(StepPinBackward, GPIO.OUT)
		def forward(x):
			GPIO.output(StepPinForward, GPIO.HIGH)
			print "forwarding running  motor1 "
			time.sleep(x)
			GPIO.output(StepPinForward, GPIO.LOW)
		forward(1)
		GPIO.cleanup()

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(TRIG4, GPIO.OUT)
	GPIO.setup(ECHO4, GPIO.IN)
	GPIO.output(TRIG4, False)
	time.sleep(0.05)
	GPIO.output(TRIG4, True)
	time.sleep(0.00001)
	GPIO.output(TRIG4, False)
	while GPIO.input(ECHO4) == 0:
		pulse_start4 = time.time()
	while GPIO.input(ECHO4) == 1:
		pulse_end4 = time.time()
	pulse_duration4 = pulse_end4 - pulse_start4
	distance4 = pulse_duration4 * 17150
	distance4 = round(distance4, 2)
	if distance4 < 30:
		mode = GPIO.getmode()
		print " mode =" + str(mode)
		GPIO.cleanup()
		StepPinForward = 16
		StepPinBackward = 26
		sleeptime = 1
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(StepPinForward, GPIO.OUT)
		GPIO.setup(StepPinBackward, GPIO.OUT)
		def forward(x):
			GPIO.output(StepPinForward, GPIO.HIGH)
			print "forwarding running  motor1 "
			time.sleep(x)
			GPIO.output(StepPinForward, GPIO.LOW)
		forward(1)
		GPIO.cleanup()

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(TRIG5, GPIO.OUT)
	GPIO.setup(ECHO5, GPIO.IN)
	GPIO.output(TRIG5, False)
	time.sleep(0.05)
	GPIO.output(TRIG5, True)
	time.sleep(0.00001)
	GPIO.output(TRIG5, False)
	while GPIO.input(ECHO5) == 0:
		pulse_start5 = time.time()
	while GPIO.input(ECHO5) == 1:
		pulse_end5 = time.time()
	pulse_duration5 = pulse_end5 - pulse_start5
	distance5 = pulse_duration5 * 17150
	distance5 = round(distance5, 2)
	if distance5 < 30:
		mode = GPIO.getmode()
		print " mode =" + str(mode)
		GPIO.cleanup()
		StepPinForward = 18
		StepPinBackward = 26
		sleeptime = 1
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(StepPinForward, GPIO.OUT)
		GPIO.setup(StepPinBackward, GPIO.OUT)
		def forward(x):
			GPIO.output(StepPinForward, GPIO.HIGH)
			print "forwarding running  motor1 "
			time.sleep(x)
			GPIO.output(StepPinForward, GPIO.LOW)
		forward(1)
		GPIO.cleanup()

	if GPIO.input(~VOUT1|~VOUT2):
		mode = GPIO.getmode()
		print " mode =" + str(mode)
		GPIO.cleanup()

		StepPinForward = 22
		StepPinBackward = 26
		sleeptime = 1

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(StepPinForward, GPIO.OUT)
		GPIO.setup(StepPinBackward, GPIO.OUT)


		def forward(x):
			GPIO.output(StepPinForward, GPIO.HIGH)
			print "forwarding running  motor "
			time.sleep(x)
			GPIO.output(StepPinForward, GPIO.LOW)


		print "forw++ard motor "
		forward(0.25)
		GPIO.cleanup()