import unittest
from datastruct.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_stack_init(self):
        self.assertEqual(self.stack.top, None)

    def test_stack_push(self):
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')
        self.assertEqual(self.stack.top.data, 'data3')
        self.assertEqual(self.stack.top.next_node.data, 'data2')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data1')
        self.assertEqual(self.stack.top.next_node.next_node.next_node, None)

    def test_stack_pop_add_data_one(self):
        self.stack.push('data1')
        data1 = self.stack.pop()
        self.assertEqual(data1, 'data1')
        self.assertEqual(self.stack.top, None)

    def test_stack_pop_add_data_two(self):
        self.stack.push('data1')
        self.stack.push('data2')
        data2 = self.stack.pop()
        self.assertEqual(data2, 'data2')
        self.assertEqual(self.stack.top.data, 'data1')




