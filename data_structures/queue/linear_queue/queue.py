from node import Node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.node_count = 0

    def is_empty(self)->bool:
        return self.rear is None

    def peek(self):
        if self.is_empty():
            raise RuntimeError("The Queue is empty!")
        else:
            print(self.front.data)

    def enqueue(self, data)->None:
        self.node_count += 1
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next_node = new_node
            new_node.prev_node = self.rear
            self.rear = new_node

    def dequeue(self)->Node:
        if self.is_empty():
            raise RuntimeError("The Queue is empty!")
        else:
            self.node_count -= 1
            n = self.front
            if self.front == self.rear:
                self.front = None
                self.rear = None
                return n
            else:
                n = self.front
                new_first_node = self.front.next_node
                self.front.next_node.prev_node = None
                self.front.next_node = None
                self.front = new_first_node
                return n
