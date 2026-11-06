"""Given a binary tree, determine if it is height-balanced."""

"""Approach:  a tree for in which for every node abs difference between height of left tree and right
 tree at most 1 is called height balanced binary tree.... it is solved by individually calc the height
   of right and left part of tree for every node and then compare... -1 is returned when it is unbalanced
     and if a lower node is unbalanced then no need to check for parent node, it will be auto unbalanced"""

""" Time Complexity: O(N)
    Space Complexity: O(N)"""

class Solution:
    def isBalanced(self, root):
        def height(root):
            if root is None:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            if (lh == -1 or rh == -1):
                return -1
            if abs(lh-rh) > 1:
                return -1
            return max(lh,rh) + 1
        return height(root) != -1
