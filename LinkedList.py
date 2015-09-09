from ListNode import ListNode

VISUAL_SIZE = 9
HALF_VISUAL_SIZE = 5
HALF_BLOCK_SIZE = 3

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.size = 0

	def _search(self, position):
		#Check to make sure position is valid
		assert 0 <= position < self.size

		#Begin at the start
		node = self.head
		i = 0
		#Loop through until position is reached
		while i < position:
			#move to next node
			node = node.link
			i += 1

		return node


	def append (self, item):
		print "\nTo append ", item
		if self.size > 0:
			print "Point node at position", self.size-1, "to new node at position", self.size
			#Find the last node of the list
			node = self._search(self.size - 1)
			newNode = ListNode (item)
			#set the last node of the list to point to the new node as it's link
			node.link = newNode
		else:
			print "Begin list by setting head to new node"
			#This will be the start of the list
			newNode = ListNode (item)
			self.head = newNode
		self.size += 1
		self.printStruct()


	def delete (self, position):
		print"\nTo delete at position", position
		self.printDelete(position)
		#If deleting the beginning of the list
		if position == 0:
			node = self._search(position)
			#Set the next node to be the head
			self.head = node.link
		else:
			#Find the node before the one we want to delete
			prevNode = self._search(position - 1)
			#Set that's nodes link to the link of the node we're deleting
			prevNode.link = prevNode.link.link
		self.size -= 1
		self.printStruct()


	def pop(self):
		assert self.size > 0
		print("\nTo pop the last item, we must remove the link"),
		print("between the second to last item and the node to delete")
		node = self._search(self.size-2)
		node.link = None
		self.size -= 1
		self.printStruct()


	def insert(self, position, item):
		assert position <=  self.size-1
		prevNode = self._search(position-1)
		newNode = ListNode(item, prevNode.link)

		print"To insert a new node containing", item, "at position", position
		self.printInsert(position-1, newNode.item)
		prevNode.link = newNode
		self.size += 1
		self.printStruct()

		
		














	# ---
	#| ? |
	# ---
	def printStruct (self):
		#print ("\n")
		print(" ---      ") * (self.size),

		print("\n"),
		i = 0
		while i <= self.size-1:
			node = self._search(i)
			print ("|"),
			print(node.item),
			print("|"),
			if (i != self.size-1):
				print ("-->"),
			i += 1

		print("\n"),
		print(" ---      ") * (self.size)


	# -----------
	#|           |
	#            v
	def printDelete(self, position):
		print "Point item at position", position-1, "to item at position", position+1
		print ("\n")
		print (" ")*(VISUAL_SIZE*(position-1)+HALF_BLOCK_SIZE),
		print ("-") * ((VISUAL_SIZE*2)+HALF_BLOCK_SIZE)
		print (" ")*(VISUAL_SIZE*(position-1)+HALF_BLOCK_SIZE),
		print ("|"),
		print (" ")*((VISUAL_SIZE*2)-1),
		print ("|")
		print (" ")*(VISUAL_SIZE*(position-1)+HALF_BLOCK_SIZE),
		print ("|"),
		print (" ")*((VISUAL_SIZE*2)-1),
		print ("v")
		self.printStruct()
		print"Delete item at position", position


	def printInsert(self, prevPosition, item):
		print ("Create a node, and link it to the previous node's link\n")
		print (" ")*(VISUAL_SIZE*(prevPosition)+HALF_VISUAL_SIZE),
		print (" ---")
		print (" ")*(VISUAL_SIZE*(prevPosition)+HALF_VISUAL_SIZE),
		print ("|"),
		print(item),
		print("|---")
		print (" ")*(VISUAL_SIZE*(prevPosition)+HALF_VISUAL_SIZE),
		print(" ---   |")
		print(" ")*(VISUAL_SIZE*(prevPosition+1)+HALF_BLOCK_SIZE),
		print("v")
		self.printStruct()

		print("Next, link the previous node to point at the new node\n")
		print (" ")*(VISUAL_SIZE*(prevPosition)+HALF_VISUAL_SIZE),
		print (" ---")
		print (" ")*(VISUAL_SIZE*(prevPosition)+HALF_BLOCK_SIZE-1),
		print ("-->|"),
		print(item),
		print("|---")
		print(" ")*(VISUAL_SIZE*(prevPosition)+HALF_BLOCK_SIZE-1),
		print("|   ---   |")
		print(" ")*(VISUAL_SIZE*(prevPosition)+HALF_BLOCK_SIZE-1),
		print("|"),
		print(" ")*(VISUAL_SIZE-2),
		print("v")
		self.printStruct()

		print("Slide the new node into place, removing the previous link between nodes\n")



		


				 
