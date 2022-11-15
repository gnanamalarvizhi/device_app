import socket
import json
import time
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())
s = socket.socket()
print("Socket Created")
s.bind(('',int(os.getenv('SOCKET_SERVER_PORT'))))
s.listen(3)
print("waiting for connections")
c, addr = s.accept()
data =[{
"Battery_Level":3.52,
 "Device_Id":1156053076,
 "First_Sensor_temperature":19.4 ,
 "Route_From":"Hyderabad, India",
 "Route_To":"Louisville, USA"
 },
{
"Battery_Level":2.57,
 "Device_Id":1156053077,
 "First_Sensor_temperature":20.4 ,
 "Route_From":"Banglore, India",
 "Route_To":"Louisville, USA"
}]
while True:
    try:
        print("connected with", addr)
        userdata = (json.dumps(data)+"\n").encode('utf-8')
#        print(userdata)
        c.send(userdata)
        time.sleep(100)
    except Exception as e:
        print(e)
        c.close()