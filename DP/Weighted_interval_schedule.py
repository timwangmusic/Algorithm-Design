"""
Given a list of intervals with starting and ending time and non-negative weight,
return a subset of compatible intervals with maximimal total weight.
"""
class Interval:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class WIS:
    def __init__(self, intervals):
        assert(len(intervals) > 0)
        self.intervals = intervals
        self.num_intervals = len(intervals)

    def findPrevInterval(self):
        self.intervals.sort(key = lambda x: x.end)
        self.prevs = [-1] * self.num_intervals
        for i, interval in enumerate(self.intervals):
            for j in range(i-1, -1, -1):
                if self.intervals[j].end <= interval.start:
                    self.prevs[i] = j
                    break

    def maxScheduling(self, new_intervals = None):
        """
        Params:
            new_intervals type: List[Interval]
            ret type: int
        """
        if new_intervals:
            self.intervals = new_intervals
        self.num_intervals = len(self.intervals)

        self.findPrevInterval()

        dp = [0] * (self.num_intervals+1)
        for i, interval in enumerate(self.intervals):
            if self.prevs[i] == -1:
                dp[i+1] = max(interval.weight, dp[i])
            else:
                dp[i+1] = max(dp[self.prevs[i]+1] + interval.weight, dp[i])
        self.dp = dp
        return self.dp[-1]

    def find_solution(self, j):
        """
        print intervals in the range of 1 to j that belong to the optimal solution.
        """
        if j == 0:
            return
        prev = self.prevs[j-1]
        if self.intervals[j-1].weight + self.dp[prev+1] >= self.dp[j-1]:
            print ('%d' % j)
            self.find_solution(prev+1)
        else:
            self.find_solution(j-1)

# Testing
i1 = Interval(1,3,5)
i2 = Interval(2,4,6)
i3 = Interval(3,10,10)
i4 = Interval(4,13,12)
i5 = Interval(2,11,20)
OBJ = WIS([i1, i2, i3, i4, i5])
print("The weighted scheduling interval sum is: %d" % OBJ.maxScheduling())
print ('The solution is:')
OBJ.find_solution(OBJ.num_intervals)
