from math import ceil as round


class Node():
    """Node class for storing unrolled linked list arrays
    """
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

    def validate_item(self, index):
        """This function checks if the index is in range.
        It checks if the index is positive and negative.
        If the index is positive, it will return the index.
        If the index is negative, it will return the positive index of the element, counting from the end of the list
        """
        if 0 <= index < self.length:
            # index is positive
            return index
        elif 0 > index >= -self.length:
            # index is negative
            return self.length + index
        else:
            raise IndexError('Index is out of range')

    def balance(self, prev_node, current_node):
        while current_node is not None:
            next_node = current_node.next
            if next_node is None and len(current_node) == 0:
                prev_node = next_node
            elif next_node is not None and  len(current_node) < round(self.max_node_capacity/2):
                while len(current_node) < round(self.max_node_capacity/2):
                    current_node.array.append(next_node.array.pop(0))
            current_node = next_node


    def __delitem__(self, index):
        index = self.validate_item(index)
        prev_node = None
        node = self.head
        while node is not None:
            if index < len(node):
                del node.array[index]
                self.length -= 1
                self.balance(prev_node,node)
                break
            else:
                index -= len(node)
                prev_node = node
                node = node.next

    def __getitem__(self, index):
        index = self.validate_item(index)
        node = self.head
        while node is not None:
            if index < len(node):
                return node.array[index]
            else:
                index -= len(node)
                node = node.next

    def __setitem__(self, key, value):
        index = self.validate_item(key)
        node = self.head
        while node is not None:
            if index < len(node):
                node.array[index] = value
                break
            else:
                index -= len(node)
                node = node.next

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
            if len(node) < self.max_node_capacity:
                node.array.append(data)
            else:
                new_node = Node()
                new_node.array = node.array[int(round(len(node)/2)):]
                new_node.array.append(data)
                node.array = node.array[:int(round(len(node)/2))]
                node.next = new_node

        self.length += 1


mylist = UnrolledLinkedList(3)
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.append(6)
mylist.append(7)
print(mylist)
del mylist[1]
print(mylist)

"""
mylist.append(8)
mylist.append(9)
print(mylist)
mylist[-1] = 100
mylist[-6] = 200
mylist[-8] = 300
mylist[-9] = 400
print(mylist)
"""




"""


for num in mylist:
    print(num, end=' ')
print('')
for num in reversed(mylist):
    print(num, end=' ')
print('')

__delitem__ (self,index)
Remove the item at the given index.
If the index is negative, then you should remove starting from the back (i.e. deleting at -2 would delete the second-to-last element)
If the index is too large, raise an IndexError
"""
