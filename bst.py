class NewNode:

    # Construct to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Returns true if given tree is BST.
def isBST(root, l=None, r=None):
    # Base condition
    if root is None:
        return True

    # if left node exist then check it has
    # correct data or not i.e. left node's data
    # should be less than root's data
    if l is not None and root.data <= l.data:
        return False

    # if right node exist then check it has
    # correct data or not i.e. right node's data
    # should be greater than root's data
    if r is not None and root.data >= r.data:
        return False

    # check recursively for every node.
    return isBST (root.left, l, root) and isBST (root.right, root, r)
