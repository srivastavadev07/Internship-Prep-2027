class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



root = Node(1)

root.left = Node(2)
root.right = Node(3)
 
root.left.left = Node(4)
root.left.right = Node(5)



def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)

inorder_traversal(root)




def search_bst(root, target):

    if root is None:
        return False

    if root.data == target:
        return True

    if target < root.data:
        return search_bst(root.left, target)

    return search_bst(root.right, target)