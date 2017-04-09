#from player import *
import pickle
import os.path

def menuMain(player):

	while player.menu:

		login_message = ''

		if player.login == False:
			login_message = 'Account'
		else:
			login_message = 'Back'
		
		player.socket.sendall(
			'1: ' + login_message + '\n' +
			'2: Exit\n')

		selection = player.socket.recv(1024).strip()

		# Logga in eller ut
		if selection == '1':

			# Login
			if player.login == False:
				menuAccount(player)

			# Back
			else:
				player.menu = False
				menu_login = False

		elif selection == '2':
			player.exit = True
			player.menu = False

		else:
			player.socket.sendall('Unknown option selected!\n')

def menuAccount(player):
	
	menu_login = True

	while menu_login:
		player.socket.sendall(
			'1: Login\n' +
			'2: Create account\n' +
			'3: Back\n')

		selection = player.socket.recv(1024).strip()

		if selection == '1': # Login
			menuAccountLogin(player)
		elif selection == '2': # Create account
			menuAccountCreate(player)
		elif selection == '3': # Back
			menu_login = False
		else:
			player.socket.sendall('Unknown option selected!\n')

def menuAccountCreate(player):
	player.socket.sendall('Your account name.\n')
	player_input_account = player.socket.recv(1024).strip()

	if not os.path.isfile('players/' + player_input_account + '_login'):
		player.socket.sendall('Your password.\n')
		player_input_password = player.socket.recv(1024).strip()

		f = open('players/' + player_input_account + '_login', 'w')
		f.write(player_input_password)
		f.close()

		player.socket.sendall('Account created.\n')

	else:
		player.socket.sendall('Username already in use\n')

def menuAccountLogin(player):
	player.socket.sendall('Account: ')
	player_input_account = player.socket.recv(1024).strip()

	player.socket.sendall('Password: ')
	player_input_password = player.socket.recv(1024).strip()

	if os.path.isfile('players/' + player_input_account + '_login'):
		f = open('players/' + player_input_account + '_login', 'r')
		if f.read().strip() == player_input_password:
			player.login = True
			player.name = player_input_account
			player.socket.sendall('Logged in.\n')
			#reply = player.name + ' has entered the game.'
			#for users in player_list:
            #    users.socket.sendall(reply)
		else:
			player.socket.sendall('Login failed.\n')
		f.close()
	else:
		player.socket.sendall('Login failed.\n')