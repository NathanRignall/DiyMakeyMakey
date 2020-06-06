import socket

host = ''
port = 8989
locaddr = (host,port) 
client = '192.168.0.1'

# Create a UDP socket

try:
    msg = 'test'
    msg = msg.encode(encoding="utf-8") 
    sent = sock.sendto(msg, tello_address)
except KeyboardInterrupt:
    print ('\n . . .\n')
    sock.close()  

def initializeSocket():
    global sock, tello_address
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tello_address = (client, port)
    sock.bind(locaddr)
