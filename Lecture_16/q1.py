#!/usr/bin/python3
def ask_questions():

	data={}
	data["name"]=input("What's your name? ")
	data["age"]=input("How old are you? ")
	data["color"]=input("What's your favorite color? ")
	data["python"]=input("Do you like Python? ")
	data["world_flat"]=input("The world is flat: True or False? ")

	print("Nice to meet you,",data["name"])
	print(data["age"],"is a great age!")
	print(data["color"]+"? Nice choice!")
	if data["python"].lower() == "yes":
		print("Great! You are in the right course!")
	elif data["python"].lower() == "no":
		print("Give it a few more weeks...")

	if data["world_flat"].lower() == "true":
		print("Hmm... maybe check that again")
	elif data["world_flat"].lower() == "false":
		print("Correct! Well done!")

ask_questions()
