# Use binary search to find square root (floor to integer) of a non-negative integer.
def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    def binSearch(min_, max_, target):
        start, end = min_, max_
        while start <= end:
            mid = start + (end - start) // 2
            if mid ** 2 == target:
                return mid
            elif mid ** 2 > target:
                end = mid - 1
            else:
                start = mid + 1
        return end
    return binSearch(1, x, x)
        
