#!/usr/bin/env python

import socket   # Networking sockets
import sys      # System errors
from thread import *    # Multithreading

from player import *    # Player manager
from menu import *      # Menu manager
 
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
    player = new_player(conn, 'Guest'+str(addr[1]))

    while not player.login:
        menuMain(player)

    player_list.append(player)

    #Sending message to connected client
    reply = player.name + ' has logged in.'
    for users in player_list:
        users.socket.sendall(reply)
    player.socket.send('Welcome to the server. Type something and hit enter\n') #send only takes string

    #infinite loop so that function do not terminate and thread do not end.
    while not player.exit:

        reply = ''
        data = ''

        # Open menu
        if player.menu:
            menuMain(player)

        # Don't ask the user to type if it's exiting the server.
        if not player.exit:
            #Receiving from client
            data = player.socket.recv(1024).strip()
            reply = player.name + ': ' + data + '\n'

        # Don't perform any operations if we don't get any input from user.
        if not data:
            break

        # The input from user that will open the menu.
        if data == 'menu':
            player.menu = True
            reply = ''
        
        # Reply to all connected users.
        if reply:
            for users in player_list:
                users.socket.sendall(reply)
        

    #came out of loop
    for users in player_list:
        users.socket.sendall(player.name + ' has disconnected.\n')

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