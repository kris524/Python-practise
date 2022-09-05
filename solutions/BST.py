# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        
            
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            
        elif root.val == key:  
            #Here we return the value that will overwrite the soon to be deleted key
            if root.left == None and root.right == None: return None
            elif root.left == None and root.right != None: return root.right
            elif root.left != None and root.right == None: return root.left

            #if both
            pointer = root.right
            #while a left branch exists, move all the way to the most left node 
            while pointer.left: pointer = pointer.left
            #we leave and overwrite the root by that most left value on the right branch
            root.val = pointer.val
            root.right = self.deleteNode(root.right, root.val)
            
            
        return root