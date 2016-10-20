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
        """Balances nodes after deleting an element
        """
        while current_node is not None:
            next_node = current_node.next
            if next_node is None and len(current_node) == 0:
                if self.length == 0:
                    self.head = None
                else:
                    prev_node.next = None
            elif next_node is not None and len(current_node) < self.max_node_capacity/2:
                while len(current_node) <= self.max_node_capacity/2:
                    current_node.array.append(next_node.array.pop(0))
                    if len(next_node) == 0:
                        next_node = next_node.next
                        current_node.next = next_node
                if len(next_node) >= self.max_node_capacity/2:
                     break
            current_node = next_node

    def __delitem__(self, index):
        """Delete item from list
        """
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
        """Get item from array. Works with positive and negative values
        """
        index = self.validate_item(index)
        node = self.head
        while node is not None:
            if index < len(node):
                return node.array[index]
            else:
                index -= len(node)
                node = node.next

    def __setitem__(self, key, value):
        """Set item at index to a certain value
        """
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
        """Returns iterator for Unrolled Linked List
        """
        node = self.head
        iter_array = []
        while node is not None:
            iter_array += node.array
            node = node.next
        for element in iter_array:
            yield element

    def __str__(self):
        """Prints string representation of Unrolled Linked List
        """
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
        """Get number of elements in Unrolled Linked List"""
        return self.length

    def __reversed__(self):
        """Returns reverse iterator for Unrolled Linked List
        """
        node = self.head
        iter_array = []
        while node is not None:
            iter_array += node.array
            node = node.next
        for element in reversed(iter_array):
            yield element

    def __contains__(self, obj):
        """Returns True if element is found in list, otherwise it returns false
        """
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
        """Adds data to end of Unrolled Linked List
        """
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