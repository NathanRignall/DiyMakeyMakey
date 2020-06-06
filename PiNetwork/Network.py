import socket

def sendInitializeSocket(client = '192.168.0.1', port = 8989):
    global sendSock, endAddress
    host = ''
    locaddr = (host,port) 
    sendSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    endAddress = (client, port)
    sendSock.bind(locaddr)
    print("SendSocketOpened")

def sendEndSocket():
    global sendSock
    sendSock.close()
    print("SendSocketClosed")

def sendData(data):
    global sendSock, endAddress
    msg = data.encode(encoding="utf-8")
    sendSock.sendto(msg, endAddress)
    print("Sent: ", msg)

def rcvInitializeSocket(port = 8989):
    global rcvSock
    host = ''
    locaddr = (host,port) 
    rcvSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rcvSock.bind(locaddr)
    print("RcvSocketOpened")

def rcvData():
    global rcvSock
    data = rcvSock.recvfrom(1518)
    rcvdata = (data.decode(encoding="utf-8"))
    return rcvdata

def rcvEndSocket():
    global rcvSock
    sendSock.close()
    print("RcvSocketClosed")