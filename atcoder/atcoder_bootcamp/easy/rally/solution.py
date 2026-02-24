import sys


def solve():
    io = sys.stdin.read().split()

    if not io:
        return

    x = list(map(int, io[1:]))

    res = float("inf")
    for i in range(101):
        t = 0
        for v in x:
            t += (v - i) * (v - i)
        res = min(t, res)

    print(res)


if __name__ == "__main__":
    solve()
