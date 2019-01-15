class BSTNode:
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None
		self.parent = None
	def hasLeftChild(self):
		return self.left
	def hasRightChild(self):
		return self.right
	def isLeftChild(self):
		return self.parent and self.parent.left == self
	def isLeftChild(self):
		return self.parent and self.parent.right == self
	def insert(self, val):
		cursor = self
		while(1):
			#import pdb; pdb.set_trace()
			if val < cursor.data:
				if cursor.left == None:
					newNode = BSTNode(val)
					cursor.left = newNode
					newNode.parent = cursor
					break
				else:
					cursor = cursor.left
			else:
				if cursor.right == None:
					newNode = BSTNode(val)
					cursor.right = newNode
					newNode.parent = cursor
					break
				else:
					cursor = cursor.right
def printTree(root):
	if root == None:
		return
	printTree(root.left)
	print(root.data)
	printTree(root.right)
root = BSTNode(10)
root.insert(2)
root.insert(5)
root.insert(7)
root.insert(1)
printTree(root)


