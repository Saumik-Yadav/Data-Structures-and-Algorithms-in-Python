def bubble(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        swap = 0
        for j in range(0,i-1):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = 1
        if (swap == 0):
            break
    print("after sorting: ")
    print(*arr)
arr = [12,34,33,22,2,43]
bubble(arr)