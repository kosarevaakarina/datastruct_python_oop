class Node:
    def __init__(self, data, next_node=None):
        """Инициализация узла"""
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """Добавление элемента в стек"""
        node = Node(data)
        node.next_node = self.top
        self.top = node

