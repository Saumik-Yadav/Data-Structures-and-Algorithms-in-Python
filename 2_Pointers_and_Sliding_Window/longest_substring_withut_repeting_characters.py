'''Given a string s, find the length of the longest substring without duplicate characters.'''

'''Approach: create a dictionary in which we store all the unique element if element is repeted then we will take their later
 value... define 2 pointers l and r, and start iterate through r, every time check if the element is previously present in
   dictionary then reassign l and add new position of r in dict'''

'''Time complexity: O(n)
    Space complexity: O(n)'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        l = 0
        r = 0
        maxlen = 0
        while(r <len(s)):
            if (hash.get(s[r],-1) != -1):
                if (hash[s[r]] >= l):
                    l = hash[s[r]] + 1
            total = r -l +1
            maxlen = max(maxlen,total)
            hash[s[r]] = r
            r += 1
        return maxlen