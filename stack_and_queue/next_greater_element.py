'''problem: The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.'''

'''APPROACH: first we will create 3 data structures, 1 list for answer storing, 1 dictionary for mapping nums2 values with their greatest element and 1 stack which helps us to reduce the TC.... we will apply backward tracking in nums2 and check if the greatest element is present in the stack and pop until we found that element, if in this way stack will get empty then we will return -1 for that value. at the end we will push that element into the stack and move to next element to nums2.... at last using dict and nums1 we will insert element into our answer list'''

''' Time complexity: O(n) for backtracing in nums2 and O(n) in the worst case in stack, so total O(2N)
    Space complexity: O(2n) for stack and dictionary'''

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        map = {}
        stk = []
        for i in range(len(nums2)-1,-1,-1):
            while(stk != [] and nums2[i]>= stk[-1]):
                stk.pop()
            if (stk == []):
                map[nums2[i]] = -1
            else:
                map[nums2[i]] = stk[-1]
            stk.append(nums2[i])
        for i in nums1:
            ans.append(map[i])
        return ans