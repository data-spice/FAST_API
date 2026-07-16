def partition(arr,low,high):
    pivot=arr[high]
    i=low-1

    for j in range (low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j]= arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1


def quicksort(arr,low,high):
    if low < high:
        piv=partition(arr,low,high)
        quicksort(arr,low,piv-1)
        quicksort(arr,piv+1,high)

nums = [5, 2, 9, 1, 9, 7]

quicksort(nums, 0, len(nums) - 1)

print(nums)