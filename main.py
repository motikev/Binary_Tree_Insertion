class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    
    if key < root.value:
        root.left = insert(root.left, key)
    elif key > root.value:
        root.right = insert(root.right, key)
    
    return root

# Create an empty BST
root = None

# Insert values
values_to_insert = [50, 30, 20, 40, 70, 60, 80]
for value in values_to_insert:
    root = insert(root, value)

# In-order traversal to print values in ascending order
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")
        in_order_traversal(root.right)

print("In-order traversal (ascending order):")
in_order_traversal(root)
