import Network as net
import RPi.GPIO as GPIO

keys = [0,0,0]

def key0(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        keys[0] = 1
    else:
        keys[0] = 0
def key1(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        keys[1] = 1
    else:
        keys[1] = 0
def key2(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        keys[2] = 1
    else:
        keys[2] = 0

net.sendInitializeSocket(port=9000, client="192.168.54.3")
net.sendData("Starup")
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(11, GPIO.IN, GPIO.BOTH, callback=key0)
GPIO.setup(13, GPIO.IN, GPIO.BOTH, callback=key1)
GPIO.setup(15, GPIO.IN, GPIO.BOTH, callback=key2)
while True:
    net.sendData(str(keys))
    print(keys)
    time.sleep(0.05)
net.sendEndSocket()