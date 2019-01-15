class Vertex:
	def __init__(self, key):
		#set identifier equal to key i.e. 'A'
		self.id = key
		#create an empty dictionary that will later
		#contain ids of conncted verticies
		self.connectedTo = {}

	def addNeighbor(self, num, weight):
		#set the num index of the dictionary connectedTo to 
		#the corresponding weight
		self.connectedTo[num] = weight

	def getConnections(self):
		#return the nums corresponding to
		#the connected verticies
		return self.connectedTo.keys()

	def getId(self):
		#return the name of a vertex
		return self.id

	def getWeight(self, num):
		#return the weight corresponding
		#to a certain num
		return self.connectedTo[num]

class Graph:
	def __init__(self):
		#create an empty dictionary that will
		#later be used to store the names of 
		#the verticies as well as their cost
		self.vertList = {}
		#keep a count of the total amt of verticies
		self.numVerts = 0

	def addVertex(self, key):
		#create a new vertex node
		new = Vertex(key)
		#add the node to the dictionary
		self.vertList[key] = new
		#increment the total amount of verticies
		self.numVerts += 1
		return new

	def getVertex(self, n):
		#if the key exists in the dictionary
		#return the corresponding vertex
		if n in self.vertList:
			return self.vertList[n]
		#otherwise return None
		else:
			return None

	def addEdge(self, f, t, cost = 0):
		#if either f or t are not keys in the vertList
		#create no verticies for them
		if f not in self.vertList:
			nv = self.addVertex(f)
		if t not in self.vertList:
			nv = self.addVertex(t)
		#conncted these verticies with an edge of predetermined cost
		self.vertList[f].addNeighbor(self.vertList[t], cost)

	def getVerticies(self):
		#return the keys to the vertList dictionary
		return self.vertList.keys()

	def __iter__(self):
		#makes the graph class iterable
		return iter(self.vertList.values())


g = Graph()
for i in range(6):
	g.addVertex(i)
print(g.vertList)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
print(g.getVertex(1))
for v in g:
	for w in v.getConnections():
		print("( %s , %s )" % (v.getId(), w.getId()))







