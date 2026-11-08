class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
node1 = Node(10)
print(node1.data)
print(node1.next)




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3
head = node1



current = head
while current is not None:
    print(current.data)
    current = current.next



    new_node = Node(40)
current = head
while current.next is not None:
    current = current.next
current.next = new_node




def search(head, target):
    current = head
    while current is not None:
        if current.data == target:
            return True
        current = current.next
    return False