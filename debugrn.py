from datetime import datetime
import socket

def printLog(*args, **kwargs):
    msg = ' '.join([str(item) for item in args])
#Change arguments of print
    #open file
    file = open("log.txt", "a")
    #get date as a string
    date = datetime.now()
    file.write(str(date) + " " + msg + "\n")
    file.close()
    
