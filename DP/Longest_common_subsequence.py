# implement longest common subsequence algoirthm
def LCS_Memo(X, Y):
    m, n = len(X), len(Y)
    memo = {}
    opt = []
    def dp(i, j):
        if (i, j) in memo: return memo[i, j]
        if i < 0 or j < 0: return 0     # LCS of empty string and any string can only be empty
        if X[i] == Y[j]:
            memo[i, j] = dp(i-1, j-1) + 1
        else:
            memo[i, j] = max(dp(i, j-1), dp(i-1, j))
        return memo[i, j]

    def findSolution():
        i, j = m-1, n-1
        while i >= 0 and j >= 0:
            if X[i] == Y[j]:
                opt.append(X[i])
                i, j = i-1, j-1
            else:
                if i * j > 0:
                    if memo[i-1, j] > memo[i, j-1]:
                        i = i - 1
                    else:
                        j = j - 1
                elif i > 0:
                    i -= 1
                else:
                    j -= 1

    dp(m-1, n-1)
    findSolution()
    return opt[::-1]


# Testing
X = "ABCDEORK"
Y = 'ACDEGRFO'
solution = LCS_Memo(X, Y)
print (solution)
print ("""The longest common subsequence of strings {x} and {y} is {z}""".
         format(x = X, y = Y, z = solution))
