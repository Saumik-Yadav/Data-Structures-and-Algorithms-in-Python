'''arr = [12,5,67,34,54,34]
for i in range(0,5):
    mini = i
    for j in range(i,6):
        if (arr[j] < arr[mini]):
            mini = j
    temp = arr[mini]
    arr[mini] = arr[i]
    arr[i] = temp
print(arr)'''

def selection(arr):
    n = len(arr)
    for i in range(0,n-1):
        mini = i
        for j in range(i+1,n):
            if(arr[j] < arr[mini]):
                mini = j
        arr[i],arr[mini] = arr[mini],arr[i]
    print("after sorting:")
    print(*arr)
arr = [12,5,67,34,54,34]
selection(arr)