import sys


def solve():
    io = sys.stdin.read().split()

    n = int(io[0])
    a = int(io[1])
    b = int(io[2])
    s = list(io[3])

    passed = 0
    overseas = 0

    for i in range(n):
        p = s[i]

        # if they are a japanese student; passed < a + b
        if p == "a" and passed < a + b:
            passed += 1
            print("Yes")
            continue
        # if they are overseas student; passed < a + b && i > b
        elif p == "b" and passed < a + b and overseas < b:
            passed += 1
            overseas += 1
            print("Yes")
            continue
        # non -> no
        print("No")


if __name__ == "__main__":
    solve()
