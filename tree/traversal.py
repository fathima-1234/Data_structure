class Tree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.value, end = " ")
        in_order_traversal(node.right)

tree = Tree(5)
tree.left = Tree(10)
tree.right = Tree(20)
tree.left.left = Tree(30)
in_order_traversal(tree)