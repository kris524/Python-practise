# Build a BST
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)

            else:
                self.right.insert(value)

        return self

    def contains(self, value):
        # if self.value == value:
        #     return True
        if self.value > value:

            if self.left is None:
                return False
            else:
                self.left.contains(value)
        elif self.value < value:
            if self.right is None:
                return False
            else:
                self.right.contains(value)
        else:
            return True
        # Write your code here.

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self
