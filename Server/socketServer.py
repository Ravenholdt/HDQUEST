#!/usr/bin/env python

import socket   # Networking sockets
import sys      # System errors
from thread import *    # Multithreading

from player import *    # Player manager
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

player_list = [];

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
 
#Function for handling connections. This will be used to create threads
def clientthread(conn, addr):

    #Adding to user list and creating player-object.
    player = new_player(conn, str(addr[1]))

    player_list.append(player)

    player.socket.send('Connected as ' + player.name + '.\n')

    #Sending message to connected client
    player.socket.send('Welcome to the server. Type something and hit enter\n') #send only takes string
    
    player_conneted = True

    #infinite loop so that function do not terminate and thread do not end.
    while player_conneted:
         
        #Receiving from client
        data = player.socket.recv(1024).strip()
        reply = 'OK...' + data + '\n'

        print data == 'data'
        print data + 'data'

        if not data: 
            print 'No data.\n'

        if data == 'exit':
            player_conneted = False
            print data
        else:
            for users in player_list:
                users.socket.sendall(reply)
            player.socket.sendall(reply)
     
    #came out of loop
    player.socket.close()
    player_list.remove(player)
    #player.close()
 

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn, addr,))
 
s.close()