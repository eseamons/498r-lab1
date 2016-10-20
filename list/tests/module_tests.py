''' You will need the following import if using python2 '''
# from __future__ import absolute_import

from ..unrolled_linked_list.module import UnrolledLinkedList
import unittest


class UnrolledLinkedList_Test(unittest.TestCase):
    """Test cases for each method in the Unrolled Linked List. Also includes edge cases
    """
    def test_default_node_capacity(self):
        """Test that the default node capacity is being set, and is set to 16
        """
        l = UnrolledLinkedList()
        self.assertEqual(l.max_node_capacity, 16)

    def test_append_and_delete(self):
        l = UnrolledLinkedList()
        l.append(0)
        self.assertEquals(str(l),'{[0]}')
        del l[0]
        self.assertEquals(str(l), '{}')

    def test_append(self):
        """This will test what happens when an element is inserted and the last node is full
        """

        l = UnrolledLinkedList(3)
        l.append(0)
        l.append(1)
        l.append(2)
        l.append(3)
        self.assertEquals(str(l),'{[0, 1], [2, 3]}')

