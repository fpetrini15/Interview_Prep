class Node:
        def __init__(self, initdata):
            #set data to initial data and next to NULL
            self.data = initdata
            self.next = None

        def val(self):
            #return the data variable within the Node class
            return self.data

        def next(self):
            #return the next Node
            return self.next

        def setData(self, val):
            #change the data value within the object
            self.data = val

        def setNext(self, newNext):
            #set the next value to be another object
            self.next = newNext
def notEmpty(lists):
    val = False
    for each in lists:
        if each is not None:
            val = True
    return val

def merge(lists):
    import pdb; pdb.set_trace()
    start = 0
    while notEmpty(lists):
        minimum = 9999999
        index = -1
        for i in range(0, len(lists)):
            cursor = lists[i]
            if cursor != None and minimum > cursor.data:
                minimum = cursor.data
                index = i
        newNode = Node(minimum)
        newNode.next = None
        if start == 0:
            ptr = newNode
            head = newNode
            start = 1
        else:
            ptr.next = newNode
            ptr = newNode
        del_ptr = lists[index]
        lists[index] = del_ptr.next
    return head

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(5)

Node1.setNext(Node2)
Node2.setNext(Node3)
li = [Node1, Node4]
newli = merge(li)
cursor = newli
while cursor is not None:
    print(cursor.data)
    cursor = cursor.next
    