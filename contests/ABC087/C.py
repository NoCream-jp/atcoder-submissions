
    
N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]

dp = [[0 for _ in range(N)] for _ in range(2)]

dp[0][0] = A[0][0]
dp[1][0] = A[0][0] + A[1][0]

for j in range(1, N):
    dp[0][j] = dp[0][j-1] + A[0][j]
    dp[1][j] = max(dp[0][j] + A[1][j], dp[1][j-1] + A[1][j])
# for d in dp:
#     print(d)

print(dp[-1][-1])