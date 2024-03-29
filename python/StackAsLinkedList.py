from LinkedLists.Node import Node
class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head  # place the new node at the head (top) of the linked list
            self.head = new_node

        self.num_elements += 1

    # TODO: Add the pop method
    def pop(self):
        if self.is_empty():
            return None
        popped = self.head

        self.head = popped.next
        self.num_elements -= 1
        return popped.value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0