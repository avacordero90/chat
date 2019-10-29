#!/usr/bin/env python3

"""
Program: chatclient.py
	Written by: Ava Cordero
	Date: 10/25/2019

Description:
	Library for a simple chat client that works for one pair of users.

"""

# imports
import sys
from socket import *



# configures handle for messaging system
def config_user ():
	handle = ""
	
	handle = input ("Enter handle (max 10 chars): ")

	# prompt user for a handle no longer than 10 chars
	while len(handle) > 10 or len(handle) == 0:
		handle = input ("Enter handle: ")
		if len(handle) > 10:
			print ("Exceeded maximum characters allowed (10), try again.")
	
	return handle

# prompt user for message, then send and recv to/from server
def recv_message (clientSocket, prompt):
	sentence = ""

	# # prompt user for a message that is no longer than the maximum
	# while len(sentence) > message_max or len(sentence) == 0:
	# 	sentence = input (prompt)
	# 	if len(sentence) > message_max:
	# 		print ("Exceeded maximum characters allowed (" +
	# 			str(message_max) + "), try again.")

	# clientSocket.send (sentence.encode ("UTF-8")) # send the message
	sentence = clientSocket.recv (1024).decode ("UTF-8") # receive the message back from server

	print (prompt + sentence)

	return (sentence) # must be UTF-8

# prompt user for message, then send and recv to/from server
def send_message (clientSocket, prompt, message_max):
	sentence = ""

	# prompt user for a message that is no longer than the maximum
	while len(sentence) > message_max or len(sentence) == 0:
		sentence = input (prompt)
		if len(sentence) > message_max:
			print ("Exceeded maximum characters allowed (" +
				str(message_max) + "), try again.")

	clientSocket.send (sentence.encode ("UTF-8")) # send the message
	# prompt = clientSocket.recv (1024) # receive the message back from server

	return (sentence) # must be UTF-8


# maintains the chat functionality
def run_client (clientSocket, handle_srv, handle_cl):
	prompt_cl = handle_cl + ">"
	prompt_srv = handle_srv + ">"

	# continuously prompt for a message until the message is "\quit"
	msg = ""
	while 1:
		msg = send_message (clientSocket, prompt_srv, 500)
		# print ("msg: " + msg)
		if msg == "\\quit": # if message is "\quit", 
			print ("Connection closed...")
			exit(0)
		msg = recv_message (clientSocket, prompt_cl)

# maintains the chat functionality
def run_client_srv (clientSocket, handle_srv, handle_cl):
	prompt_cl = handle_cl + ">"
	prompt_srv = handle_srv + ">"

	# continuously prompt for a message until the message is "\quit"
	msg = ""
	while 1:
		msg = recv_message (clientSocket, prompt_srv)
		if msg == "\\quit": # if message is "\quit", 
			print ("Connection closed...")
			exit(0)
		msg = send_message (clientSocket, prompt_cl, 500)