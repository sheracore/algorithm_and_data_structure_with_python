"""
Linked list:
- In linked list nodes can be all over the place in the memory
- Lookup:
    By value O(n)
    By index O(n)
- Insert:
    At the beginning: O(1) because head pointed to it
    At the end: O(1) because tail pointed to it
    In the middle: O(n)
- Delete:
    At the beginning: O(1)
    At the end: O(n) because tail pointed to last node, and we don't know about before the last node
    In the middle: O(n)
"""


class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_of_llist = 0

    @property
    def is_empty(self):
        return self.head is None

    def add_last(self, value):
        new_node = Node(value)
        if self.is_empty:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size_of_llist += 1

    def add_first(self, value):
        new_node = Node(value)
        if self.is_empty:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size_of_llist += 1

    def index(self, value):
        node = self.head
        index = 0
        while node:
            if node.value == value:
                return index
            index += 1
            node = node.next
        return -1

    def contains(self, value):
        return self.index(value) != -1

    def remove_first(self):
        if self.is_empty:
            raise ValueError("Linked list is empty")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            head_node = self.head
            self.head = head_node.next
            head_node.next = None

        self.size_of_llist -= 1

    def remove_last(self):
        if self.is_empty:
            raise ValueError("Linked list is empty")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            previous_node = self.previous(self.tail)
            self.tail = previous_node
            previous_node.next = None

        self.size_of_llist -= 1

    def previous(self, node):
        current = self.head
        while current:
            if current.next == node:
                return current
            current = current.next
        return None

    def size(self):
        """ O(1) for this solution but to iterate over all node solution would be O(n)"""
        return self.size_of_llist


llist = LinkedList()
llist.add_last(50)
llist.add_last(60)
llist.add_first(40)
llist.add_first(30)
llist.index(40)
llist.index(60)
llist.contains(30)
llist.remove_first()
llist.remove_last()
llist.size()
print("Here")
