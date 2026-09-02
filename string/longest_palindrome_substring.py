"""problem: Given a string s, return the longest palindromic substring in s.

    approach : in this problem, first i try to find centre of the palin in the whole
     array one by one... and create 2 pointers left and right.... if value both left 
     and right are equal then extend them till they are not equal... most imprtantly 
     there are 2 cases odd length palin and even length palin and you have to check both of them one by one 
    
    complexity:
    time:  O(n**2)
    space: O(1)"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        max_len = 1
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    longest = s[left:right + 1]
                left -= 1
                right += 1
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    longest = s[left:right + 1]
                left -= 1
                right += 1
        return longest