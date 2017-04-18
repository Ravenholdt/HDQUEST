#!/usr/bin/env python

import socket   # Networking sockets
import sys      # System errors
from thread import *    # Multithreading

 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn, addr,))
 
s.close()


def clientthread(conn, addr):

	while not player.exit:


        #Receiving from client
        data = conn.recv(1024).strip()
        reply = data + '\n'

        # Don't perform any operations if we don't get any input from user.
        if not data:
            break
        
        # Reply to all connected users.
        if reply:
        	conn.sendall(reply)