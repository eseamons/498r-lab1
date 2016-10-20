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
        self.assertEqual(str(l),'{[0]}')
        del l[0]
        self.assertEqual(str(l), '{}')

    def test_append(self):
        """This will test what happens when an element is inserted and the last node is full. Should take half of the contents
        and move them to the next node.
        """

        l = UnrolledLinkedList(3)
        l.append(0)
        l.append(1)
        l.append(2)
        l.append(3)
        self.assertEqual(str(l),'{[0, 1], [2, 3]}')

    def test_getitem(self):
        """Checks to see if positive and negative indexes work.
        Also makes sure that indexes that are out of bounds throw the proper exception
        """
        l = UnrolledLinkedList(3)
        l.append(0)
        l.append(1)
        l.append(2)
        l.append(3)
        self.assertEqual(str(l[-1]),'3')
        self.assertEqual(str(l[2]),'2')

        failed = False
        try:
            print(l[4])
        except IndexError:
            failed = True
        self.assertTrue(failed)

        failed = False
        try:
            print(l[-5])
        except IndexError:
            failed = True
        self.assertTrue(failed)

    def test_balancing_after_delete_max_six(self):
        l = UnrolledLinkedList(6)
        l.append(0)
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.append(5)
        l.append(6)
        l.append(7)
        l.append(8)
        l.append(9)
        l.append(10)
        l.append(11)
        l.append(12)
        l.append(13)
        l.append(14)
        l.append(15)
        l.append(16)
        l.append(17)
        l.append(18)
        l.append(19)
        self.assertEqual(str(l), '{[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17, 18, 19]}')
        del l[4]
        self.assertEqual(str(l), '{[0, 1, 2], [3, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14], [15, 16, 17, 18, 19]}')

    def test_delete_index_zero_four_times_max_sixteen(self):
        """Tests deleting python
        """
        l = UnrolledLinkedList()
        l.append(0)
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.append(5)
        l.append(6)
        l.append(7)
        l.append(8)
        l.append(9)
        l.append(10)
        l.append(11)
        l.append(12)
        l.append(13)
        l.append(14)
        l.append(15)
        l.append(16)
        l.append(17)
        del l[0]
        del l[0]
        del l[0]
        del l[0]
        self.assertEqual(str(l), '{[4, 5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17]}')

    def test_contains(self):
        """Tests to see if item exists in list
        """
        l = UnrolledLinkedList(3)
        l.append(0)
        l.append(1)
        l.append(2)
        l.append(3)
        self.assertTrue(3 in l)
        self.assertFalse(4 in l)

    def test_iterator(self):
        l = UnrolledLinkedList(3)
        l.append(0)
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.append(5)
        l.append(6)
        l.append(7)
        iter_string = ''
        for item in l:
            iter_string += str(item) + ' '
        self.assertEqual(iter_string, '0 1 2 3 4 5 6 7 ')

    def test_reversed_iterator(self):
        l = UnrolledLinkedList(3)
        l.append(0)
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.append(5)
        l.append(6)
        l.append(7)
        iter_string = ''
        for item in reversed(l):
            iter_string += str(item) + ' '
        self.assertEqual(iter_string, '7 6 5 4 3 2 1 0 ')


    def test_len(self):
        l = UnrolledLinkedList(3)
        self.assertEqual(len(l),0)
        l.append(0)
        l.append(1)
        self.assertEqual(len(l),2)





