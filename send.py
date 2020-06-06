import socket

def initializeSocket(client = '192.168.0.1', port = 8989):
    global sock, tello_address
    host = ''
    locaddr = (host,port) 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tello_address = (client, port)
    sock.bind(locaddr)
    print("socket opened")

def endSocket():
    global sock, tello_address
    sock.close()
    print("socket closed")

def sendData(data):
    global sock, tello_address
    msg = data.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    print("sent: ", msg)