import send

try:
    send.initializeSocket(port=9000, client="192.168.54.3")
    send.sendData("Test!")
    send.endSocket()
except:
    send.endSocket()