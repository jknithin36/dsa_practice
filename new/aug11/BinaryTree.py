from collections import deque

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Tree setup
tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)
tree.left.left = BinaryTreeNode(4)
tree.left.right = BinaryTreeNode(5)
tree.right.right = BinaryTreeNode(6)

# Preorder Traversal
def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.value, end=" ")
    preOrder(rootNode.left)
    preOrder(rootNode.right)

# Level Order Traversal
def levelOrder(rootNode):
    if not rootNode:
        return []
    result = []
    queue = deque([rootNode])
    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

# Search Node
def searchNode(rootNode, nodeValue):
    if not rootNode:
        return False
    queue = deque([rootNode])
    while queue:
        current = queue.popleft()
        if current.value == nodeValue:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False


# insert a Node

def insert_a_node(rootNode, nodeValue):
    new_node = BinaryTreeNode(nodeValue)

    if not rootNode:
        return new_node
    
    queue = deque([rootNode])
    while queue:
        current = queue.popleft()
        if current.left is None:
            current.left = new_node
            return rootNode
        else:
            queue.append(current.left)
        
        if current.right is None:
            current.right = new_node
            return rootNode
        else:
            queue.append(current.right)



    
# Testing
preOrder(tree)
print("\nLevel Order:", levelOrder(tree))
print("Search 3:", searchNode(tree, 3))
print("Search 9:", searchNode(tree, 9))
print("Before Insert:", levelOrder(tree))
tree = insert_a_node(tree, 7)
print("After Insert:", levelOrder(tree))



