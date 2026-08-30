class Solution:
    def count(self,matrix,value,n,m):
        cnt = 0
        for i in range(n):
            low = 0
            high = m -1
            while (low <= high):
                mid = low + (high- low)//2
                if (matrix[i][mid] <= value):
                    low = mid + 1
                else:
                    high = mid - 1
            cnt += low
        return cnt
    def findMedian(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        low = min(matrix[0])
        high = max(matrix[0])
        for i in range(1,n):
            low = min(low,min(matrix[i]))
            high = max(high,max(matrix[i]))
        middle = (m*n)//2
        while(low <= high):
            mid = low + (high-low)//2
            target = self.count(matrix,mid,n,m)
            if (target <= middle):
                low = mid + 1
            else:
                high = mid - 1
        return low 