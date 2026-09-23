'''Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.'''

'''
APPROACH: find for each element in how many subarrays is this elemnet the minimum, you can calculate this by calculating 
the previous smaller element and next smaller or equal element.... and at last perform a basic loop  and get your answer
'''

'''Time Complexity: O(N), i know , we are performing 3 functions but each function contribute O(N)
    Space Complexity: O(n) , but in reality it is a multiple of O(n)'''

class Solution:
    def prevSmaller(self,arr):
        n = len(arr)
        stk = []
        ans = [0]*n
        for i in range(n):
            while(stk != [] and arr[stk[-1]] >= arr[i]):
                stk.pop()
            if (stk == []):
                ans[i] = -1
            else:
                ans[i] = stk[-1]
            stk.append(i)
        return ans
    def nextSmallerEqual(self,arr):
        n = len(arr)
        stk = []
        ans = [0]*n
        for i in range(n-1,-1,-1):
            while(stk != [] and arr[stk[-1]] > arr[i]):
                stk.pop()
            if (stk == []):
                ans[i] = -1
            else:
                ans[i] = stk[-1]
            stk.append(i)
        return ans
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        total = 0
        prev = self.prevSmaller(arr)
        next = self.nextSmallerEqual(arr)
        for i in range(n):
            left = prev[i]
            right = next[i]
            if (right == -1):
                right = n
            total += arr[i]*(i-left)*(right-i)
        return total% (10**9 + 7)