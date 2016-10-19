from math import ceil as round


class Node():
    def __init__(self):
        self.array = []
        self.next = None

    def __len__(self):
        return len(self.array)


class UnrolledLinkedList():
    """This class is used to implement an Unrolled Linked List
    """
    def __init__(self, max_node_capacity=16):
        self.max_node_capacity = max_node_capacity
        self.length = 0
        self.head = None

    def __delitem__(self,index):
        if index > self.length - 1:
            raise IndexError('Index is out of range')
        else:
            print("Deleting Item at index " + str(index))

    def __getitem__(self,index):
        if index >= 0 and index > self.length - 1:
            raise IndexError('Index is out of range')
        elif index < 0 and index < - self.length:
            raise IndexError('Index is out of range')
        else:
            print('In range')

    #def __setitem__ (self,key,value):

    def __iter__(self):
        node = self.head
        iter_array = []
        while node is not None:
            iter_array += node.array
            node = node.next
        for element in iter_array:
            yield element

    def __str__(self):
        node = self.head
        string = '{'
        while node is not None:
            node_array = node.array
            string += '['
            for index, element in enumerate(node_array):
                string += str(element) + '' if index == len(node_array) - 1 else str(element) + ', '
            string += ']'
            node = node.next
            string += '' if node is None else ', '
        string += '}'
        return string

    def __len__(self):
        return self.length

    def __reversed__(self):
        node = self.head
        iter_array = []
        while node is not None:
            iter_array += node.array
            node = node.next
        for element in reversed(iter_array):
            yield element

    def __contains__(self, obj):
        if self.head is None:
            return False
        else:
            contains_object = False
            node = self.head
            while node is not None:
                if obj in node.array:
                    contains_object = True
                node = node.next
            return contains_object

    def append(self, data):
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
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
print(mylist)
mylist.append(6)
mylist.append(7)
mylist.append(8)
mylist.append(9)
print(mylist)
del mylist[5]
for num in mylist:
    print(num, end=' ')
print('')
for num in reversed(mylist):
    print(num, end=' ')
print('')
del mylist[-10]
mylist[-9]
test = [1,2,3,4,5,6,7,8,9]

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
"""
