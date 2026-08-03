MOD = 1_000_000_007

N, M = map(int, input().split())

A = set([int(input()) for _ in range(M)])

"""
dp[j] = jマス目に到達する通り数
      = dp[j-1] + dp[j-2] (j not in A) 
"""

dp = [0 for _ in range(N+1)]

dp[0] = 1
if 1 in A:
    dp[1] = 0
else:
    dp[1] = 1

for j in range(2, N+1):
    if j not in A:
        if dp[j-1]:
            dp[j] = (dp[j] + dp[j-1]) % MOD
        if dp[j-2]:
            dp[j] = (dp[j] + dp[j-2]) % MOD

print(dp[-1])
