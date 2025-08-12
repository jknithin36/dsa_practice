class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    


tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)
tree.left.left = BinaryTreeNode(4)
tree.left.right = BinaryTreeNode(5)
tree.right.right = BinaryTreeNode(6)


def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.value, end="")
    preOrder(rootNode.left)
    preOrder(rootNode.right)



preOrder(tree)
print(" ")


from collections import deque
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
    return " ".join(map(str, result))




# print(levelOrder(tree))



def searchNode(rootNode, nodeValue):
    if not rootNode:
        return "Binary Tree Not exists"
    
    queue = deque([rootNode])

    while queue:
        current = queue.popleft()
        if current.value == nodeValue:
            return "found"
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)



# print(searchNode(tree, 3))



    