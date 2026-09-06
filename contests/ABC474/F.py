import sys

input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    base = 0
    minA = 10**9
    diff = []
    for _ in range(N):
        A, B = map(int, input().split())
        base += A
        minA = min(minA, A)
        diff.append(B - A)
    diff.sort()
    ans = base
    cur = base
    for k in range(1, N + 1):
        cur += diff[k - 1]
        ans = min(ans, cur + max(0, 2 * k - N) * minA)
    print(ans)
