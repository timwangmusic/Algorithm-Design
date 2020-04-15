# bisect_left: Searching for first position such that all numbers to the left are less than target
# bisect_right: Searching for first position such that all numbers to the left are less than or equals to target
from typing import List


def bisect_left(arr: List[int], target: int, left: int, right: int) -> int:
    while left < right:
        m = left + (right - left) // 2
        if arr[m] < target:
            left = m + 1
        else:
            right = m
    return left


def bisect_right(arr: List[int], target: int, left: int, right: int) -> int:
    while left < right:
        m = left + (right - left) // 2
        if arr[m] <= target:
            left = m + 1
        else:
            right = m
    return left


def searchRange(arr: List[int], target: int, left: int, right: int, left_most: bool) -> int:
    while left <= right:
        m = left + (right - left) // 2
        if arr[m] > target or left_most and arr[m] == target:
            right = m - 1
        else:
            left = m + 1
    return left if left_most else right


nums = [1, 2, 2, 2, 4, 5]

print("bisect left outputs index:", bisect_left(nums, 2, 0, len(nums)))    # expect 1
print("bisect right outputs index:", bisect_right(nums, 2, 0, len(nums)))  # expect 4

print("The left-most position for %d is %d" % (2, searchRange(nums, 2, 0, len(nums) - 1, True)))
print("The right-most position for %d is %d" % (2, searchRange(nums, 2, 0, len(nums) - 1, False)))
