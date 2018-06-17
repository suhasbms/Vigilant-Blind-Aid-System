import os
import Image
import pytesseract
from subprocess import call
print "WELCOME TO VIGILANT BLIND AID SYSTEM"
os.system('echo "WELCOME TO VIGILANT BLIND AID SYSTEM" | festival --tts')
print "....."
print "....."
print "CAPTURING IMAGE"
os.system('echo "CAPTURING IMAGE" | festival --tts')
print "....."
print "....."
os.system('sudo raspistill -co 100 -sh 75 -ev -5 -ISO 700 -sa -100 -br 70 -ifx denoise -q 90 -o test.jpg')
print "CONVERTING IMAGE TO TEXT USING TESSERACT O C R"
os.system('echo "CONVERTING IMAGE TO TEXT USING TESSERACT O C R" | festival --tts')
print "....."
print "....."

print pytesseract.image_to_string(Image.open('test.jpg'))
x= open('tts.txt', 'w')
x.write(pytesseract.image_to_string(Image.open('test.jpg')))



