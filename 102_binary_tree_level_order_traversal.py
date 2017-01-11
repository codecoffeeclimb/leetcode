# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root, None]  # Use None as separator.
        result = []
        while queue[0] is not None:
            result.append([])
            while queue[0] is not None:
                node = queue.pop(0)
                result[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            queue.pop(0)
            queue.append(None)
            
        return result

