class Stack:
	def __init__ (self):
		#initialized as a list
		self.items = []

	def isEmpty(self):
		#check if the items list is equivalent to []
		return self.items == []

	def push(self, item):
		#select insertion/deletion end
		#Easiest with append
		self.items.append(item)

	def pop(self):
		#works with append to pop last elt
		return self.items.pop()

	def size(self):
		#returns the length of the items list
		return len(self.items)

s = Stack()
print(s.isEmpty())
s.push(1)
s.push(2)
s.push(3)
print(s.items)
s.pop()
print(s.items)
print(s.size())
