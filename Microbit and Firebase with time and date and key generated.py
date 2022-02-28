import pyrebase
import serial
import datetime

firebaseConfig = {"apiKey": "AIzaSyCmJArYmOEmB0WjyOGOScq10C8sJlm59xY",
  "authDomain": "testpyrebasedb.firebaseapp.com",
  "databaseURL": "https://testpyrebasedb-default-rtdb.firebaseio.com/",
  "projectId": "testpyrebasedb",
  "storageBucket": "testpyrebasedb.appspot.com",
  "messagingSenderId": "686104036762",
  "appId": "1:686104036762:web:6d262aeed4942c7e0ba623",
  "measurementId": "G-MYNQZ2R1HX"
    }

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM9'
ser.open()
while True:
    data = str(ser.readline())
    data = data.replace("b", "")
    data = data.replace("'", "")
    data = data.replace(" ", "")
    data = data.replace("Room", "")
    data = data.replace("\\r\\n", "")
       
    remove = int(data.index(":"))
    roomNumber = data[:remove]
    temp = data[remove+1:]
    
    if roomNumber == "12":
        room = "Kitchen"
    elif roomNumber == "13":
       room = "Bedroom"
    elif roomNumber == "14":
        room = "Bathroom"
        
    tday = datetime.datetime.now()
    date = ("Date: %s/%s/%s" % (tday.day, tday.month, tday.year))
    time = ("Time: %s:%s:%s" % (tday.hour, tday.minute, tday.second))
        
    data_to_upload = {"Date":date, "Time":time, "Temp":temp,}
    db.child(room).push(data_to_upload)
    print(data)
ser.close()