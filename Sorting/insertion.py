def insertion(arr):
    n = len(arr)
    for i in range(0,n):
        j = i
        while(j>0 and (arr[j-1] > arr[j])):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j = j-1
    print("after sorting:")
    print(*arr)
arr = [12,43,23,53,23,52]
insertion(arr)