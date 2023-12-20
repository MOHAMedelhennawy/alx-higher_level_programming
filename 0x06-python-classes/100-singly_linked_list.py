#!/usr/bin/python3
"""Define a Class"""


class Node:
    """ defines a node of a singly linked list
        Attributes:
            data (int): data
            next_node (Node, optional): node
    """
    def __init__(self, data, next_node=None):
        """Initialize Node
        args:
            data (int): data stored in node
            next_node (Node): next node
        """
        self.data = data
        self.next_node = next_node


    @property
    def data(self):
        """data getter
        returns:
            data (int)
        """
        return self.__data

    
    @data.setter
    def data(self, value):
        """data setter
        args:
            value (int): value to set
        returns:
            None
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """data getter
        returns:
            data (int)
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """data setter
        args:
            value (Node): value to set
        returns:
            None
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define a Class Square"""

    def __init__(self):
        """Initialize linked list"""
        self.head = None
    
    def sorted_insert(self, value):
        """insert node in coorect sorted position
        args:
            value (int): value for new node
        """
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
        """Define the print() representation of a SinglyLinkedList."""
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(result)