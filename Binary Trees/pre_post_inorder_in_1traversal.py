'''Given a binary tree with root node. Return the In-order,Pre-order and Post-order traversal of the binary tree.'''


"""Approach: create a nested list in which elements are stored along with number 1 and it is incresed to 2 and 3
 and based on number elements are placed in individual list inorder, preorder and postorder"""


"""Time complexity: O(3N)
    Space complexity: O(4N)"""
class Solution:
    def tree_traversal(self, root):
        mp = []
        ino = []
        posto = []
        preo = []
        if root is None:
            return []
        mp.append([root,1])
        while (mp):
            top = mp[-1]
            if top[1] == 1:
                preo.append(top[0].data)
                top[1] += 1
                if (top[0].left):
                    mp.append([top[0].left,1])
            elif top[1] == 2:
                ino.append(top[0].data)
                top[1] += 1
                if (top[0].right):
                    mp.append([top[0].right,1])
            else:
                posto.append(top[0].data)
                mp.pop()
        ans = []
        ans.append(ino)
        ans.append(preo)
        ans.append(posto)
        return ans