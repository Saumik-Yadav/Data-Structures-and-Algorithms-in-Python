def reverse(nums,i,e):
    for j in range(i,i+ ((e-i+1)//2)):
        nums[i],nums[e-i] = nums[e-i],nums[i]
arr = [1,2,3,4,5,6]
def rotate(arr,k):
    n = len(arr)
    reverse(arr,0,n-k-1)
    reverse(arr,n-k,n-1)
    reverse(arr,0,n-1)
print(arr)