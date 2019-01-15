#CREATE LIST
def lists():
	#Note that each elt can have different type
	li = [1, "banana", (1,2)]
	print(li)
	#ACCESS ITEMS
	li[2]
	#ex list[0] --> 1
	#	list[1] --> banana
	#	list[-1] --> (1,2)
#CHANGE VALUE
	li[0] = 'two'
	print(li)
#LOOPING THROUGH THE LIST
	#Method 1:
	for i in range(0, len(li)):
		print(li[i])
	#Method 2:
	for index, elt in enumerate(li):
		print(elt, li[index])
	#Method 3:
	for i in range(len(li)-1, -1, -1):
		print(li[i])
	#Method 4:
	for elt in li:
		print(elt)
	#Method 5:
	for elt in li[::-1]:
		print(elt)
	#etc...
#CHECK IF AN ITEM EXISTS
	if "banana" in li:
		print("Yes")
#CHECK LENGTH
	print(len(li)) #runtime O(1)
#ADD ITMES
	#Method 1: apppend([Item])
	li.append("tea")
	#adds to the end of the list
	#Method 2: insert([index],[item])
	li.insert(0, 49)
	#inserts at specified index
#REMOVE ITEMS
	#Method 1: remove([Item])
	li.remove("banana")
	#Only removes first occurence
	#Method 2: pop()
	li.pop() #removes last item
	li.pop(0) #removes at index
	#Method 3: del
	del li[0]
#REVERSE LIST
	li.pop(0)
	li.append(10)
	li.append(20)
	#Method 1: reverse()
	li.reverse()
	print(li)
	#Method 2: [::-1]
	li = li[::-1]
	print(li)
#SORT LIST
	li.sort() #O(nlogn)
#EDITING LIST
	#Method 1: clear
	li.clear() #clears list of elts
	print(li)
	#Method 2: del
	del li #deletes list


lists()