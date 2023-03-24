from datastruct.node import Node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """Добавление элемента в стек"""
        node = Node(data)
        node.next_node = self.top
        self.top = node

    def pop(self):
        """Удаляет из стека верхний элемент и возвращает данные удаленного экземпляра класса Node"""
        del_data = self.top
        self.top = self.top.next_node
        return del_data.data
