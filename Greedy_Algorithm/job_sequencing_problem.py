'''Given an 2D array Jobs of size Nx3, where Jobs[i][0] represents JobID , Jobs[i][1] represents Deadline , Jobs[i][2] 
represents Profit associated with that job. Each Job takes 1 unit of time to complete and only one job can be scheduled at a time.

The profit associated with a job is earned only if it is completed by its deadline. Find the number of jobs and maximum profit.'''

'''
Approach:  first we will sort the list based on profit. now we have a empty dictionary in which we place key = deadline and value
= profit, first we will start checking places from deadline and reduce it till we find a suitable place... if there is no place and 
list is already sorted so it means already larger profits occupy the place we will simple leave it'''

'''
time complexity: O(nlogn + nD)
space complexity: O(D)'''

class Solution:
    def JobScheduling(self, Jobs):
        Jobs.sort(key = lambda x:x[2], reverse = True)
        d = {}
        cnt = 0
        total = 0
        for i in Jobs:
            while (i[1] > 0):
                if (i[1] not in d):
                    d[i[1]] = i[2]
                    cnt += 1
                    total += i[2]
                    break
                i[1] -= 1
        return cnt, total