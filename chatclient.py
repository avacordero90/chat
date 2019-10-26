#!/usr/bin/env python3

"""
Program: chatclient.py
	Written by: Ava Cordero
	Date: 10/25/2019

Description:
	A simple chat client that works for one pair of users.

"""

# imports
import sys
from socket import *



# connects the client to the server and maintains the chat functionality
def run_client (clientSocket):
	# variables
	msg = ""

	# gets user handle and configs prompt
	handle = message ("Enter handle: ", clientSocket)
	prompt = (handle + "> ")

	# continuously prompt for a message until the message is "\quit"
	while 1:
		msg = loc_msg = message (prompt, clientSocket)
		# print ("msg:", loc_msg)
		if loc_msg == "\\quit":
			print ("Connection closing...")
			# clientSocket.close() # this line may not be necessary
			print ("Connection closed...")
			exit(0)

def message (message, clientSocket):
	sentence = input (message)
	
	clientSocket.send (sentence.encode ("UTF-8"))
	message = clientSocket.recv (500)

	return (message.decode ("UTF-8"))


def main ():
	if len(sys.argv) != 3:
		print ("Error: Incorrect usage (chatclient.py serverport).")
		exit(1)

	serverName = sys.argv[1]
	serverPort = int (sys.argv[2])

	clientSocket = socket (AF_INET, SOCK_STREAM)
	clientSocket.connect ((serverName,serverPort))

	run_client(clientSocket)

main()