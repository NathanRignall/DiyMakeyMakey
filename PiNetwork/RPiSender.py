import Network as net

try:
    net.sendInitializeSocket(port=9000, client="192.168.54.3")
    net.sendData("Test!")
    net.sendEndSocket()
except:
    net.sendEndSocket()