class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		#insert at the front
		self.items.insert(0, item)
		#alternatively...
		#self.items.append(item)

	def dequeue(self):
		#remove at the back
		self.items.pop()
		#alternatively...
		#del self.items[0]

	def size(self):
		return len(self.items)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(q.items)
print(q.size())