# Number of sockets

import sys


def solve():

    io = sys.stdin.read().split()

    if not io:
        return

    a = int(io[0])
    b = int(io[1])

    t = 1
    res = 0
    while t < b:
        t += a - 1
        res += 1

    print(res)


if __name__ == "__main__":
    solve()
