class Node:
    def __init__(self,data,ref = None):
        self.data = data
        self.ref = None

class Link:
    def __init__(self):
        self.head = None

    def Print(self):
        n = self.head
        if self.head is None:
            print("the linked list is empty")
        else:
            while n is not None:
                print(n.data)
                n=n.ref

    def Add_begin(self,data):
        newnode=Node(data)
        newnode.ref = self.head
        self.head = newnode

    def add_end(self,data):
        newnode = Node(data)
        n= self.head
        if self.head is None:
            self.head = newnode
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = newnode

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present")
        else:
            newnode = Node(data)
            newnode.ref = n.ref
            n.ref = newnode

    def add_before(self,data,x):
        n = self.head
        newnode = Node(data)
        if self.head is None:
            print("node is not present")
            return
        if self.head == x:
            newnode.ref = self.head
            self.head = newnode
            return
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            printf("node is not present")
        else:    
            newnode.ref = n.ref
            n.ref = newnode

    def delete_begin(self):
        if self.head is None:
            print("the linked list is empty")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is  None:
            print("node is empty")
            return
        if self.head.ref is None:
            self.head.ref = None
            return
        n = self.head
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def deletenode_between(self,x):               
        if self.head is None:
            print("node is empty")
            return
        if self.head.data == x:
             self.head = self.head.ref
             return
        n = self.head
        while n.ref is not None:
            if n.ref.data ==x:
                break
            n = n.ref
        if n.ref.ref is None:
            print("node is not present")
        else:
            n.ref = n.ref.ref









