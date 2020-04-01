# bisect_left: Searching for first position such that all numbers to the left are less than target
# bisect_right: Searching for first position such that all numbers to the left are less than or equals to target


def bisect_left(nums, target, left, right):
    while left <= right:
        m = left + (right - left) // 2
        if nums[m] >= target:
            right = m - 1
        else:
            left = m + 1
    return left


def bisect_right(nums, target, left, right):
    while left < right:
        m = left + (right - left) // 2
        if nums[m] <= target:
            left = m + 1
        else:
            right = m
    return left


def searchRange(nums, target, l, r, left):
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] > target or left and nums[m] == target:
            r = m - 1
        else:
            l = m + 1
    return l if left else r


nums = [1, 2, 2, 2, 4, 5]
print("The left-most position for %d is %d" % (2, searchRange(nums, 2, 0, len(nums)-1, True)))
print("The right-most position for %d is %d" % (2, searchRange(nums, 2, 0, len(nums)-1, False)))
