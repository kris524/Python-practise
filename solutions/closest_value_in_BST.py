def findClosestValueInBst(tree, target):
    # Write your code here.
    findClosestValueHelper(tree, target, close=None)
    #


def findClosestValueHelper(tree, target, close=99999):
    close = None #keep the difference in here
    value  = abs(tree.value - target)
    if value < close:
        close = value
        
    if tree.value > target:
        
        tree = tree.left
        findClosestValueHelper(tree, target, close)
        
    elif tree.value < target:
        tree = tree.right
        findClosestValueHelper(tree, target, close)

    return close


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
