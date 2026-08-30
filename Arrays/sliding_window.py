A = [2,3,1,2,4,3]
k = 7
left = 0
sm = 0
right = 0
for i in range(len(A)):
    sm+= A[i]
    right += 1
    if (sm > k):
        left += 1
        right -=1
print(right)