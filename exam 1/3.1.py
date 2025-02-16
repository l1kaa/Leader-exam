#1. Find the Majority Element
# Given a list of N integers, find the majority element (the element that appears more than N/2 times). If there is no majority element, return None.
# Input: A list of integers arr.
# Output: Return the majority element or None.

def majority_elem(nums):
    number = None
    count = 0
    for num in nums:
        if count == 0:
            number = num
        count += 1 if num == number else -1
    return number if nums.count(number) > len(nums) // 2 else None

