'''You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by
 an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit
 each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while 
moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.'''

'''Approach: in the most optimal solution the key idea is that you don't have to reduce the size of our window, once it reach max it will 
only increase wheneven occurs never decreases... in that l and r moves together and reduces time complexity from 2N to N
'''
'''Time Complexity: O(N)
Space Complexity: O(3)'''

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        l = 0
        r = 0
        max_len = 0
        map = {}
        while (r < len(fruits)):
            map[fruits[r]] = map.get(fruits[r],0) + 1
            if (len(map) > 2):
                map[fruits[l]] -= 1
                if (map[fruits[l]] == 0):
                    del map[fruits[l]]
                l+= 1
            if (len(map) <= 2):
                max_len = max(max_len,r-l+1)
            r += 1
        return max_len