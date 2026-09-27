'''Given one meeting room and N meetings represented by two arrays, start and end, where start[i] represents the start time
 of the ith meeting and end[i] represents the end time of the ith meeting, determine the maximum number of meetings that can
   be accommodated in the meeting room if only one meeting can be held at a time. A meeting starting at the same time another
     meeting ends is considered overlapping.
'''

'''
Approach: first combine both the start and end into 1 tuple of list, because after that we want to sort them in order of end time.
after sorting, our first meeting will always be concidered so we start with 2nd meeting in the loop and if meeting start time is less 
or equal to previous meeting time then we remove it otherwise consider it....
'''

'''
Time complexity: O(n + nlogn + n)
Space Complexity: O(2n)'''

class Solution:
    def maxMeetings(self, start, end):
        combine = []
        for i in range(len(start)):
            combine.append((start[i],end[i]))
        combine.sort(key = lambda x:x[1])
        meet_time = combine[0][1]
        cnt = 1
        for i in range(1,len(combine)):
            if (combine[i][0] > meet_time):
                cnt += 1
                meet_time = combine[i][1]
        return cnt