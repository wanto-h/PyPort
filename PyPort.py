import socket
from queue import Queue
import threading
from time import time, ctime
print('''

 ____        ____            _   
|  _ \ _   _|  _ \ ___  _ __| |_ 
| |_) | | | | |_) / _ \| '__| __|
|  __/| |_| |  __/ (_) | |  | |_ 
|_|    \__, |_|   \___/|_|   \__|
       |___/                     

 ''')
print(f"Created by wanto- \n{ctime(time())}")

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
        port=1
        for port in range(startport, endport):
            port+=1
            queue.put(port)

#Scans every port and returns open ports
def portscan():
    global open_ports
    while not queue.empty():
        port=queue.get()
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=s.connect_ex((target,port))
        s.close()
        if result==0:
            print("Port open", port)
            open_ports.append(port)
    print (f"Open ports goes as follows \n {open_ports}")
    
#Defines and run threads on the portscan function
t1=threading.Thread(target=portscan)
t2=threading.Thread(target=portscan)
t3=threading.Thread(target=portscan)
t4=threading.Thread(target=portscan)

def threadstart():
    t1.start()
    t2.start()
    t3.start()
    t4.start()


#Defines which ports to add in the queue based on the mode
if scanmode==1:
   scan(allportstart,allportend)
   threadstart()
elif scanmode==2:
    scan(mainportstart,mainportend)
    threadstart()
else:
    print("This mode does not exist")
