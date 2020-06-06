import socket,time,keyboard
import Network as net

net.rcvInitializeSocket(port=9000)

while True:
    data = net.rcvData()
    data = data.decode('utf-8')
    data = data.split(',')
    if len(data) == 3:
        if data[0] == "1":
            keyboard.press('a')
        else:
            keyboard.release('a')
        if data[1] == "1":
            keyboard.press('b')
        else:
            keyboard.release('b')
        if data[2] == "1":
            keyboard.press('c')
        else:
            keyboard.release('c')
        print(data)

net.rcvEndSocket()
