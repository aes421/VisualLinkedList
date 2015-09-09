from LinkedList import LinkedList


def commhelp():
	print("The following commands are valid:")

def insert():
	print ("You are in insert")

def delete():
	print ("You are in delete")

def pop():
	print ("You are in pop")

def append():
	print ("You are in append")

def default():
	print("Incorrect command form.  Please refer to help")





LinkedList = LinkedList()

UI = raw_input("Enter a command or type help: ")

while (UI != "quit"):
	#Uses python dictionary functionality to make a clean
	#switch like structure
	#source: http://bytebaker.com/2008/11/03/switch-case-statement-in-python/
	switch = {
	"hel": commhelp,
	"ins": insert,
	"del": delete,
	"pop": pop,
	"app": append
	}

	#Chops the input to only 3 letters for the switch
	UI = UI[:3]


	try:
		#uses the dictionary structure as case statements
		switch[UI]()
	except (KeyError):
		#implements the switch statements default case
		default()

	
	UI = raw_input("Enter a command or type help: ")

