import sys
import math


def solve():
    io = sys.stdin.read().split()
    n = int(io[0])

    i, j = 1, n

    while i <= j:
        m = (i + j) // 2
        x = math.floor(m * 108 / 100)

        if x < n:
            i = m + 1
        else:
            j = m - 1

    if math.floor(i * 108 / 100) == n:
        print(i)
    else:
        print(":(")

    return


if __name__ == "__main__":
    solve()
