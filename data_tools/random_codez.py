def maxnum(arr):
    max_no=0
    for i in range(len(arr)):
        if arr[i]>max_no:
            max_no=arr[i]

    return max_no

nums = [4, 9, 2, 15, 7,45]

print(maxnum(nums))