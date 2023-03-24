import unittest
from datastruct.node import Node


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node(10)

    def test_node_init(self):
        self.assertEqual(self.node.data, 10)
        self.assertEqual(self.node.next_node, None)

    def test_node_next_node(self):
        node2 = Node(1, self.node)
        self.assertEqual(node2.next_node, self.node)
