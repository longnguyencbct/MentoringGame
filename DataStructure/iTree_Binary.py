class Node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

class BinTree:
    def __init__(self, root=None):
        self.root=root
        self.height=self.getHeight()
    def getHeight(self):
        return Helper_getHeight(self.root)

def Helper_getHeight(node=None):
    if node is None:
        return 0
    left_height = Helper_getHeight(node.left)
    right_height = Helper_getHeight(node.right)
    return max(left_height, right_height) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

tree = BinTree(root)

height = tree.getHeight()
print("Height of the tree:", height)

