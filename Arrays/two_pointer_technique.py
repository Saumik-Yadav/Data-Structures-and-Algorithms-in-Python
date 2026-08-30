'''A = [1,2,2,2,3,3,3,4]
A.sort()
i = 0
j = 1
new = []
while(i<len(A)-1):
    if (A[i] == A[j]):
        j +=1
    else:
        new.append(A[i])
        i = j
        j +=1
new.append(A[i])
print(new)'''

#sorting array
'''A = [2,0,2,1,1,0]

low = 0
mid = 0
high = len(A) - 1

while mid <= high:
    if A[mid] == 0:
        A[low], A[mid] = A[mid], A[low]
        low += 1
        mid += 1

    elif A[mid] == 1:
        mid += 1

    else:  # A[mid] == 2
        A[mid], A[high] = A[high], A[mid]
        high -= 1

print(A)'''

#move all negative numbers to left
A = [1,3,4,-2,-5,-4,0,5,6]
left = 0
right = len(A) -1
while (left<right):
    if (A[left] < 0):
        left +=1
    else:
        A[left],A[right] = A[right],A[left]
        right-=1
print(A)