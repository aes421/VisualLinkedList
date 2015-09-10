from LinkedList import LinkedList


def commhelp():
	print("The following commands are valid:")

#Form: insert(position,item)
def insert(UI):
	print ("You are in insert")
	command = UI[6:]
	print(command)

#Form: delete(position)
def delete(UI):
	print ("You are in delete")

#Form: pop()
def pop():
	print ("You are in pop")

#Form: append(positon, item)
def append(UI):
	print ("You are in append")

def default():
	print("Incorrect command form.  Please refer to help")





LinkedList = LinkedList()

UI = raw_input("Enter a command or type help: ")

while (UI != "quit"):

	#Chops the input to only 3 letters for the switch
	UIchop = UI[:3]

	#determine which function the user is trying to call
	if (UIchop == "hel"):
		commhelp()
	elif (UIchop == "ins"):
		insert(UI)
	elif (UIchop == "del"):
		delete(UI)
	elif (UIchop == "pop"):
		pop()
	elif (UIchop == "app"):
		append(UI)
	else:
		default()

	
	UI = raw_input("Enter a command or type help: ")

