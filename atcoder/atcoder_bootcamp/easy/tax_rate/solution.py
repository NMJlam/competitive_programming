import sys
import math


def solve():
    io = sys.stdin.read().split()
    n = int(io[0])

    for x in range(1, n + 1):
        if math.floor(x * 27 / 25) == n:
            print(x)
            return

    print(":(")


if __name__ == "__main__":
    solve()
