class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        s, b = min(p.val, q.val), max(p.val, q.val)

        while root:
            
            # found the lowest common ancestry
            if root.val >= s and root.val <= b: return root
            
            if root.val > b: root = root.left # larger than the big number, move down left
            elif root.val < s: root = root.right # smaller than the small number, move down right
            
