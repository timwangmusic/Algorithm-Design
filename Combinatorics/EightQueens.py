# Problem of eight queeens.
# Output all possible positions so that any two queens cannot attack each other.
# Actually you can set the board of size N and try to place N queens.
# Each output corresponds to a placement sequence of columns. The sequence itself is row sequence.
N = 8
def eightQueens(depth, path, avail, res):
    if depth == N:
        res.append(list(path))
    else:
        for row in range(N):
            if canPut(row, path, avail):
                avail[row] = False
                eightQueens(depth+1, path+[row], avail, res)
                avail[row] = True


def canPut(idx, path, avail):
    if avail[idx] == False: return False    # Vertical collision
    L = len(path)
    for k, pos in enumerate(path):
        if L - k == abs(pos - idx):     # Diagonal collision
            return False
    return True

res = []
avail = [True] * N
path = []
eightQueens(0, path, avail, res)
print (res)
