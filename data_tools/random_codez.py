def count_even(arr):
    counter=0
    for i in range(0, len(arr)):
        if arr[i]%2==0:
            counter+=1
    return counter


nums = [1, 2, 4, 7, 10, 13, 18]

print(count_even(nums))