import socket
from queue import Queue
import threading

queue=Queue()
open_ports=[]
target=socket.gethostbyname(input(("What is your target? ")))

#Defining scan modes
allportstart=1
allportend=65535
mainportstart=1
mainportend=1024

print("Select your scan type:")
print("1)All Ports")
print("2)Main Ports")
scanmode=int(input("Type the number of the scan: "))

#Adds everything to the queue
class scan():
    def __init__(self,startport,endport):
        for port in range(startport, endport):
            queue.put(port)

#Defines which ports to add in the queue based on the mode
if scanmode==1:
   scan(allportstart,allportend)
elif scanmode==2:
    scan(mainportstart,mainportend)
else:
    print("This mode does not exist")

#Scans every port and returns open ports
def portscan():
    for port in queue.get():
        s=socket(socket.AF_INET,socket.SOCK_STREAM)
        result=s.connect_ex((target,port))
        if result==0:
            print("Port open", port)
            open_ports.append(port)

print (f"Open ports goes as follows /n {open_ports}")
