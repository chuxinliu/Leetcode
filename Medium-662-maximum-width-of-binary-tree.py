class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width, level = 0, [(root, 1)]
        while len(level): # Keep going if current level has some nodes
            width = max(width, level[-1][1] - level[0][1] + 1)
            next_level = []
            for item, num in level: # Put all children of current level in next_level
                if item.left: next_level.append((item.left, num*2))
                if item.right: next_level.append((item.right, num*2+1))
            level = next_level
        return width
