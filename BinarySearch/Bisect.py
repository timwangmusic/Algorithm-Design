# bisect_left: Searching for first position such that all numbers to the left are less than target
# bisect_right: Searching for first position such that all numbers to the left are less than or equals to target
def bisect_left(nums, target, l, r):
     while l <= r:
         m = l + (r-l)//2
         if nums[m] >= target:
             r = m - 1
         else:
             l = m + 1
     return l


def bisect_right(nums, target, l, r):
    while l < r:
        m = l + (r-l)//2
        if nums[m] <= target:
            l = m + 1
        else:
            r = m
    return l

def searchRange(nums, target, l, r, left):
    while l <= r:
        m = l + (r-l)//2
        if nums[m] > target or left and nums[m] == target:
            r = m - 1
        else:
            l = m + 1
    return l if left else r

nums = [1, 2, 2, 2, 4, 5]
print ("The left-most position for %d is %d" % (2, searchRange(nums, 2, 0, len(nums)-1, True)))
print ("The right-most position for %d is %d" % (2, searchRange(nums, 2, 0, len(nums)-1, False)))
