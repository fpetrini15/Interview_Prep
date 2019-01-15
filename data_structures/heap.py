class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def swapUp(self, size):
		#size // 2 checks the parent
		while size // 2 > 0:
			if self.heapList[i] < self.heapList[size // 2]:
				temp = self.heapList[size // 2]
				self.heapList[size // 2] = self.heapList[i]
				self.heapList[i] = temp
			i = i // 2

	def insert(self, val):
		self.heapList.append(val)
		self.currentSize += 1
		self.swapUp(self.currentSize)

	def swapDown(self, size):
		while(size*2) <= self.currentSize:
			mc = minChild(size)
			if self.heapList[size] > self.heapList[mc]:
				self.heapList[size], self.heapList[mc] = self.heapList[mc], self.heapList[size]
			size = mc

	def minChild(self, size):
		if (i*2)+1 < self.currentSize:
			return i * 2
		else:
			if self.heapList[i*2]
				return i * 2
		else:
			return i * 2 + 1
	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return retval
	def buildHeap(self,alist):
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while (i > 0):
			self.percDown(i)
			i = i - 1

