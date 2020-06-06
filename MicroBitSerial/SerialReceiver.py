import serial,time,keyboard

ser = serial.Serial(port='COM3', baudrate=115200, timeout=0)

print("connected to: " + ser.portstr)
count=1

while True:
    data = ser.readline()
    data = data.decode('utf-8')
    data = data.replace("[", "")
    data = data.replace("]", "")
    data = data.split(', ')
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
    time.sleep(0.1)

ser.close()
