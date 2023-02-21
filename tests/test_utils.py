import unittest
from utils.utils import Node, Stack


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node(10)

    def test_node_init(self):
        self.assertEqual(self.node.data, 10)
        self.assertEqual(self.node.next_node, None)

    def test_node_next_node(self):
        node2 = Node(1, self.node)
        self.assertEqual(node2.next_node, self.node)


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
