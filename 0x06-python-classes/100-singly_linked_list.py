#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) or value != None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def sorted_insert(self, value):
        new_node = Node(value, None)


        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node

        else:
            currentNode = self.head
            while currentNode.next_node is not None and currentNode.next_node.data < value:
                currentNode = currentNode.next_node
            new_node.next_node = currentNode.next_node
            currentNode.next_node = new_node

    def __repr__(self):
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(result)
