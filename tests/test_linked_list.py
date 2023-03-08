import unittest
from datastruct.linked_list import LinkedList


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_ll_init(self):
        self.assertEqual(self.ll.head, None)
        self.assertEqual(self.ll.tail, None)

    def test_insert_beginning(self):
        self.ll.insert_beginning({'id': 1})
        self.assertEqual(self.ll.head.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 1})
        self.ll.insert_beginning({'id': 2})
        self.assertEqual(self.ll.head.data, {'id': 2})
        self.assertEqual(self.ll.tail.data, {'id': 1})

    def test_insert_at_end(self):
        self.ll.insert_at_end({'id': 1})
        self.assertEqual(self.ll.head.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 1})

        self.ll.insert_at_end({'id': 12})
        self.assertEqual(self.ll.head.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 12})

    def test_print_ll(self):
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})

        self.assertEqual(self.ll.print_ll(), " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")