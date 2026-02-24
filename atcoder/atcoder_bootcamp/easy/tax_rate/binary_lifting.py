import sys
import math


def solve():

    io = sys.stdin.read().split()
    n = int(io[0])

    j = n**2
    x = 0
    while j >= 1:
        while math.floor((x + j) * 108 / 100) < n:
            x += j

        j //= 2

    if math.floor((x + 1) * 108 / 100) == n:
        print(x + 1)
    else:
        print(":(")

    return


if __name__ == "__main__":
    solve()
