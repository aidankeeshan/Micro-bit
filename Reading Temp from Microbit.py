import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM12'
ser.open()
while True:
    data = str(ser.readline())
    data = data.replace("b","")
    data = data.replace("'","")
    data = data.replace(" ","")
    data = data.replace("\\r\\n","")
    space = data.index(":")
    name = data[:space]
    steps = data[space+1:]
    print(data)
    print(name)
    print(steps)
ser.close()