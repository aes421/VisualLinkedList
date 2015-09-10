from LinkedList import LinkedList
import re

LinkedList = LinkedList()

def commhelp():
	print("The following commands are valid:\n")
	print("1) insert(position,item): this function allows you to specify a"),
	print("specific position in the linked list to insert an item.  Positions"),
	print("for the linked list start with 0 as the first element.  Ex. insert(1,2)"),
	print("will insert the number 2 at position 1\n")

#Form: insert(position,item)
def insert(UI):
	#chop the UI to get only (position,item)
	command = UI[6:]
	#Regular expression: (\(\d*,.\))
	expression = re.compile('(\(\d*,.*\))')
	if (expression.match(command) != None):
		#get the position
		pos = command[1]
		i = 2
		while command[i] != ",":
			pos += command[i]
			i += 1

		#Check that position is a number
			if (~pos.isdigit()):
				break


		#get the item
		item = command[i+1]
		i += 2
		while command[i] != ")":
			item += command[i]
			i += 1

		#called insert with pos, item
		LinkedList.append(1)
		LinkedList.insert(int(pos), item)




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

