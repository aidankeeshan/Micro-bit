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


xTadhg = [0]
yTadhg = [0]

xDonnach = [0,]
yDonnach = [0,]

def microbitreader():

    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = "COM16"
    ser.open()
    xAxisTadhg = 0
    xAxisDonnach = 0
   
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
        
        if name == "Tadhg":
            xAxisTadhg += 1
            xTadhg.append(xAxisTadhg)
            yTadhg.append(float(steps))
            
        elif name == "Donnach":
            xAxisDonnach +=1
            xDonnach.append(xAxisDonnach)
            yDonnach.append(float(steps))
        #print (steps)          

        
#defines how the graph will be plotted. Picking points from both the x and y list to plot against eachother  
def animate(i): 
    ax1.clear()
    ax1.plot(xTadhg, yTadhg)
    ax1.plot(xDonnach, yDonnach)    

   
 
threading.Thread(target= microbitreader).start()
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

