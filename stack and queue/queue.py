class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.ref = newnode
            self.tail = newnode

    def dequeue(self):
        if self.head is None:
            print("queue is empty")

        x = self.head.data
        self.head = self.head.ref
        if self.head is None:
            self.tail = None
        return x

    def display(self):
        if self.head is None:
            print("Queue is empty")
        else:
            n = self.head
            while n:
                print(n.data)
                n = n.ref

q = Queue()
q.enqueue(10)
q.enqueue(14)
q.enqueue(16)
q.display()
                
q.dequeue()
                
q.display()