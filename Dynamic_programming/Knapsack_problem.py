# 0/1 Knapsack problem solution with dynamic solution
# Greedy algorithm based on value / size ratio does not work


def knapsack(goods, capacity):
    """
    Solves 0/1 Knapsack problem given a list of weight, value pairs
    :param goods: List[List[int]]
    :param capacity: int
    :return: int
    """
    n = len(goods)
    opt = [[0] * (capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        weight_i, val_i = goods[i-1]
        for weight in range(capacity+1):
            if weight < weight_i:
                opt[i][weight] = opt[i-1][weight]
            else:
                opt[i][weight] = max(opt[i-1][weight], opt[i-1][weight-weight_i] + val_i)
    return opt[n][capacity]


if __name__ == '__main__':
    goods = [[3, 3], [7, 4], [1, 5], ]
    capacity = 5
    print(knapsack(goods, capacity))
