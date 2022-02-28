# Gather Microbit data via serial port and live plotting graph as more data is entered.
import serial
#allows more that one function/operation to run in the one program - multi threading
import threading

#used to plot the graph
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


# Set up the Serial connection to capture the Microbit communications

ser = serial.Serial()


xPerson1 = [0]
yPerson1 = [0]

xPerson2 = [0,]
yPerson2 = [0,]

def microbitreader():

    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = "COM16"
    ser.open()
    xAxisPerson1 = 0
    xAxisPerson2 = 0
   
    while True:
# Read in a line from the Microbit, store it in variable 'microbitdata' as a string
        microbitdata = str(ser.readline())
        #print(microbitdata)
   
            # Cleanup the data from the microbit and convert it to an integer
        data = microbitdata[2:]
        data = data.replace(" ","")
        data = data.replace("\\r\\n","")
        data = data.replace("'","")
        space = data.index(":")
        name = data[:space]
        steps = data[space+1:]
        
        if name == "Person1":
            xAxisPerson1 += 1
            xPerson1.append(xAxisPerson1)
            yPerson1.append(float(steps))
            
        elif name == "Person2":
            xAxisPerson2 +=1
            xPerson2.append(xAxisPerson2)
            yPerson2.append(float(steps))
        #print (steps)          

        
#defines how the graph will be plotted. Picking points from both the x and y list to plot against eachother  
def animate(i): 
    ax1.clear()
    ax1.plot(xPerson1, yPerson1)
    ax1.plot(xPerson2, yPerson2)    

   
 
threading.Thread(target= microbitreader).start()
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

