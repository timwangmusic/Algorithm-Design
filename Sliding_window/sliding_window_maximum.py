"""
Given an array of integers and a positive number k, find the maximums in each k-sized window.

This is a particularly useful algorithm. For instance you want to know the most steps
you have taken in the last 7 days. And you can quickly get a local maximum.
"""

import collections
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    q = collections.deque()
    res = []
    for idx, num in enumerate(nums):
        if q and q[0] <= idx - k:
            q.popleft()
        while q and nums[q[-1]] <= num:
            q.pop()
        q.append(idx)
        if idx >= k - 1:
            res.append(nums[q[0]])
    return res
