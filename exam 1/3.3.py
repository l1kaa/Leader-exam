# 3. Rotate an Array
# Given a list arr, rotate it to the right by k steps.
# Input:
# A list of integers arr.
# An integer k.
# Output: Return the rotated array.

def rotate_arr(arr, k):
    num = len(arr)
    k = k % num
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_arr(arr,k))
