# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        res=[]
        def dfs(root):
            if root==None:
                return 
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        print(res)
        length=len(res)
        if length!=len(list(set(res))):
            return False
        if res==sorted(res):
            return True
        else:
            return False
            
        
