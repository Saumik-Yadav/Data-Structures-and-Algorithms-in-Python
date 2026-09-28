'''You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith
 interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the
   start and end of another interval.

Two intervals are considered overlapping if they share at least one point.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any
 overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.'''

'''Approach:  you have to divide the main array into 3 while loops. firstone which is lower than new interval and third which is greater than 
the new interval and mainly apply things in the middle interval where overlapping occurs... '''

'''Time complexity: 0(n)
Space complexity: O(n)'''

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new_intervals = []
        n = len(intervals)
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            new_intervals.append(intervals[i])
            i += 1
        start = newInterval[0]
        end = newInterval[1]
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        new_intervals.append([start, end])
        while i < n:
            new_intervals.append(intervals[i])
            i += 1

        return new_intervals