def main():
    import sys

    input = sys.stdin.readline

    N = int(input())
    S = input().strip()

    # Aの位置を列挙
    posA = [i for i, c in enumerate(S) if c == "A"]

    # パターン1: A が偶数位置 (0,2,4,...)
    target1 = [2 * i for i in range(N)]
    cost1 = sum(abs(a - b) for a, b in zip(posA, target1))

    # パターン2: A が奇数位置 (1,3,5,...)
    target2 = [2 * i + 1 for i in range(N)]
    cost2 = sum(abs(a - b) for a, b in zip(posA, target2))

    print(min(cost1, cost2))


if __name__ == "__main__":
    main()
