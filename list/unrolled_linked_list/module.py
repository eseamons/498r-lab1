from math import ceil as round
class Node():
    def __init__(self):
        self.array = []
        self.next = None

    def __len__(self):
        return len(self.array)

class UnrolledLinkedList():
    """This is the class name you should use. You should also have a
    max_node_capacity. Also, you should remove this comment and possibly
    replace it with your own
    """
    def __init__(self, max_node_capacity=16):
        self.max_node_capacity = max_node_capacity
        self.length = 0
        self.head = None

    #def __delitem__ (self,index):

    #def __getitem__ (self,index):

    #def __setitem__ (self,key,value):

    #def __iter__ (self):

    def __str__ (self):
        node = self.head
        string = '{'
        while node is not None:
            node_array = node.array
            string += '['
            for index, element in enumerate(node_array):
                string += str(element)+ '' if index == len(node_array) - 1 else str(element)+ ', '
            string += ']'
            node = node.next
            string += '' if node is None else ', '
        string += '}'
        return string

    def __len__ (self):
        return self.length

    #def __reversed__ (self):

    def __contains__ (self, obj):
        if self.head is None:
            return False
        else:
            return True

    def append(self,data):
        if self.head is None:
            node = Node()
            node.array.append(data)
            node.next = None
            self.head = node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            if len(node.array) < self.max_node_capacity:
                node.array.append(data)
            else:
                new_node = Node()
                new_node.array = node.array[int(round(len(node)/2)):]
                new_node.array.append(data)
                node.array = node.array[:int(round(len(node)/2))]
                node.next = new_node

        self.length += 1


mylist = UnrolledLinkedList(4)
print(mylist)
print(len(mylist))
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
print(mylist)
mylist.append(5)
print(mylist)
mylist.append(6)
mylist.append(7)
print(mylist)
mylist.append(8)
mylist.append(9)

print(mylist);
print(len(mylist))



"""
__delitem__ (self,index)
Remove the item at the given index.
If the index is negative, then you should remove starting from the back (i.e. deleting at -2 would delete the second-to-last element)
If the index is too large, raise an IndexError
__getitem__ (self,index):
Returns the item in the given index.
If the index is negative, return with the index starting from the back (i.e. getting at -1 returns the last item)
If the index is too large, raise an IndexError
__setitem__ (self,key,value):
sets the item at key to value
If the key is too large, raise an IndexError
__iter__ (self):
Use the Python yield statement to make your list iterable. This will allow you to use it in a for-each loop
__str__ (self)
Create a string representation of the list in the form {[x, x, x], [x, x], [x, x, x, x]} where each set of [] indicates the list of values within a single node.
__len__ (self)
returnsthetotal#ofdatainthelist,notthenumberofnodes
__reversed__ (self)
reverse of iter
__contains__ (self, obj)
Returns True if obj is in the data structure, otherwise False
Implement additional method:

append(self,data)
Add the data to the end of the list
If a node has reached its max capacity, you must create a new node to put the data in
"""
