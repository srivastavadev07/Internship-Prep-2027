def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    return root




root = None
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    root = insert(root, value)





# def search(root, target):

#     if root is None:
#         return False

#     if root.data == target:
#         return True

#     if target < root.data:
#         return search(root.left, target)

#     return search(root.right, target)




# print(search(root, 40))  # True
# print(search(root, 90))  # False