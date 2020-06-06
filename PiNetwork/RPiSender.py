import Network as net
import RPi.GPIO as GPIO

keys = [0,0,0]

def key0(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        key[0] = 1
    else:
        key[0] = 0
try:
    net.sendInitializeSocket(port=9000, client="192.168.54.3")
    net.sendData("Starup")
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(10, GPIO.IN, GPIO.BOTH, callback=key0)
    GPIO.setup(11, GPIO.IN, GPIO.BOTH, callback=key1)
    GPIO.setup(12, GPIO.IN, GPIO.BOTH, callback=key2)
    while True:
        net.sendData(str(keys))
        print(keys)
        time.sleep(0.05)
    net.sendEndSocket()
except:
    net.sendEndSocket()