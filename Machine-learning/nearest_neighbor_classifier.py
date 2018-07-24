import heapq
from collections import Counter
from timeit import timeit


class Point:
    def __init__(self, dim=2, val=None):
        self.val = val
        self.dim = dim

    def find_dist(self, point):
        """
        Returns distance squared between point and another point in Euclidean space.
        :param point: Point
        :return: float or int depending on input
        """
        assert point.dim == self.dim, "Dimension mismatch, cannot calculate distance"
        res = 0
        for d in range(self.dim):
            res += (self.val[d] - point.val[d]) ** 2
        return res


class NearestNeighborsClassifier:
    """
    This class finds k closest neighbors of input data and assign labels to each observation.
    """
    def __init__(self):
        self.x_train = None
        self.y_train = None

    def fit(self, x, y=None):
        self.x_train = x
        self.y_train = y

    def _find_neighbors(self, k, point):
        """
        This internal method finds k closest neighbors of input point and returns neighbors and their labels
        :param k: int
        :param point: Point
        :return: List[int]
        """
        if self.x_train is None or self.y_train is None:
            print('No training data available')
            return [], []
        elif len(self.x_train) <= k:
            return self.x_train, self.y_train

        heap = []   # max heap
        for i, p in enumerate(self.x_train):
            if i < k:
                heapq.heappush(heap, (-point.find_dist(p), i))
            else:
                dist = point.find_dist(p)
                if dist < -heap[0][0]:
                    heapq.heapreplace(heap, (-dist, i))
        point_ix = (i for d, i in heap)
        res_labels = [self.y_train[i] for i in point_ix]
        return res_labels

    def predict(self, k, point):
        """
        predict class label for the given point
        :param k: int
        :param point: Point
        :return: int
        """
        labels = self._find_neighbors(k, point)
        return Counter(labels).most_common(1)[0][0]


# Testing
if __name__ == '__main__':
    import numpy as np
    dim = 3
    points = np.random.randn(100000, 3)
    Points = [Point(dim, point) for point in points]
    labels = np.random.randint(1, 5, size=(100000, ))
    new_point = Point(dim, (1, 2, 3))
    classifier = NearestNeighborsClassifier()

    def run_code():
        classifier.fit(Points, labels)

    print("average running time is %.6f seconds" % timeit(stmt=run_code, number=10000))
