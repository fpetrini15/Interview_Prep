class Node:
	def __init__(self, initdata):
		#set data to initial data and next to NULL
		self.data = initdata
		self.next = None

	def getData(self):
		#return the data variable within the Node class
		return self.data

	def getNext(self):
		#return the next Node
		return self.next

	def setData(self, val):
		#change the data value within the object
		self.data = val

	def setNext(self, newNext):
		#set the next value to be another object
		self.next = newNext

class linked_list:
	def __init__(self):
		#initially, head pointer points to NULL
		self.head = None

	def isEmpty(self):
		#check if head is equivalent to None
		return self.head == None

	def add(self, item):
		#add node to the front of the LL
		temp = Node(item)
		#use the head pointer as the anchor before changing it
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		#set current to head and count to 0
		current = self.head
		count = 0
		#until current == None, count and move cursor
		while current != None:
			count += 1
			current = current.getNext()
		#return count
		return count

	def search(self, target):
		current = self.head
		#until current == None check each node for target
		while current != None:
			#if found, return true
			if current.getData() == target:
				return True
			#else continue through the list
			else:
				current = current.getNext()
		return False

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		#until current == None, search for item
		while current != None:
			#if found, set bool to True and break
			if current.getData() == item:
				found = True
				break
			#else move the cursors
			else:
				previous = current
				current = current.getNext()
		#if found == True and previous == None, current head node must be removed
		if found == True and previous == None:
			self.head = current.getNext()
		#otherwise set prev-->next to curr-->next
		else:
			previous.setNext(current.getNext())

newNode = Node(1)
mylist = linked_list()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print(mylist.isEmpty())
print(mylist.search(1))
print(newNode.getData())
print(mylist.size())
current = mylist.head
while current != None:
	print(current.getData())
	current = current.getNext()











