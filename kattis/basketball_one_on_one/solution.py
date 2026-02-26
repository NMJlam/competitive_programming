import sys


def solve():
    io = sys.stdin.read()
    n = len(io)
    a, b = 0, 0

    i = 0
    while i < n:
        char = io[i]

        if char == "A":
            a += int(io[i + 1])
        elif char == "B":
            b += int(io[i + 1])

        i += 2

    print("A") if a > b else print("B")


if __name__ == "__main__":
    solve()
