# Gives the program access to the serial ports (USB's) on the computer
import serial

ser = serial.Serial()

# is the rate at which information is transferred in this case the MIcro:bit can transfer 115200 bits per second.
ser.baudrate = 115200

# The USB port has to be specified and can be found though Device Manager 
ser.port = 'COM12'
ser.open()

# Strips away the extra information sent by the Micro:bit
while True:
    data = str(ser.readline())
    data = data.replace("b","")
    data = data.replace("'","")
    data = data.replace(" ","")
    data = data.replace("\\r\\n","")
    
    # Find the location of the : in the information 
    space = data.index(":")
    
    # Divides the information in relation to the :
    room = data[:space]
    temp = data[space+1:]
    
    # Prints the various variables 
    print(data)
    print(room)
    print(temp)
    
# Closes the communication between the Setrial port and the Micro:bit
ser.close()
