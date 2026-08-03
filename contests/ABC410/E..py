N, H, M = map(int, input().split())
dp = [[-1 for _ in range(H+1)] for _ in range(N+1)]
dp[0][H] = M
l = [(-1, -1)] + [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    a, b = l[i+1]
    for j in range(0, H+1):
        if dp[i][j] == -1:
            continue
        if 0 <= j - a:
            dp[i+1][j-a] = max(dp[i+1][j-a], dp[i][j])
        if 0 <= dp[i][j] - b:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] - b)

ans = 0
for i in range(1, N+1):
    if dp[i].count(-1) != H+1:
        ans += 1
print(ans)