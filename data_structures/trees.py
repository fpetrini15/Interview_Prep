class TreeNode:
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None
		self.parent = None
	def hasLeftChild(self):
		return self.left
	def hasRightChild(self):
		return self.right
	def addLeft(self, val):
		newNode = TreeNode(val)
		self.left = newNode
		newNode.parent = self
	def addRight(self, val):
		newNode = TreeNode(val)
		self.right = newNode
		newNode.parent = self
	def replaceNode(self, val, parent, rc, lc):
		self.data = val
		self.left = lc
		self.right = rc
		self.parent = parent

root = TreeNode(2)
root.addLeft(1)
root.addRight(3)
print(root.left.data)
print(root.right.data)
import pdb; pdb.set_trace()
root.left.replaceNode(6,root,root.left.left, root.left.right)
cursor = root.left
print(root.data)
print(root.left)


