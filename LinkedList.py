from ListNode import ListNode

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
		if self.size > 0:
			#Find the last node of the list
			node = self._search(self.size - 1)
			newNode = ListNode (item)
			#set the last node of the list to point to the new node as it's link
			node.link = newNode
		else:
			#This will be the start of the list
			newNode = ListNode (item)
			self.head = newNode
		self.size += 1


	def delete (self, position):
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


	def printLL (self):
		print ("\n")
		i = 0
		while i <= self.size-1:
			print(" ---     "),
			i += 1

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
		i = 0
		while i <= self.size-1:
			print(" ---     "),
			i += 1
				 
