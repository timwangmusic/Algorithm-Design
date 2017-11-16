# implement longest common subsequence algoirthm
def LCS(X, Y):
    """
    type X: a sequence or string of length m
    type Y: a sequence or string of length n
    ret: length of the longest common subsequence of X and Y
    """
    m = len(X)
    n = len(Y)
    prev = [0] * (n + 1)

    for i in range(m):
        current = [0] * (n + 1)
        for j in range(n):
            if X[i] == Y[j]:
                current[j + 1] = prev[j] + 1
            else:
                current[j + 1] = max(prev[j+1], current[j])
        prev = current
    return current[-1]

# Testing
X = "ABCDEORK"
Y = 'ACDEGRFO'
res = LCS(X, Y)
# Output: Length of the longest common subsequence of strings ABCDEORK and ACDEGRFO is 5
print ("""Length of the longest common subsequence of strings {x} and {y} is {z}""".
        format(x = X, y = Y, z = res))
