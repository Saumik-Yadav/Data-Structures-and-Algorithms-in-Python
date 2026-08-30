def quicksort(arr,low,high):
    if (low< high):
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i < high and arr[i] <= pivot:
            i += 1

        while j > low and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

arr = [23,44,12,55,33,24]
quicksort(arr,0,len(arr)-1)
print(*arr)