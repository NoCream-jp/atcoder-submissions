"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < wanna solve green
"""
###################################################

# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
MOD = 998244353
# drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def c_list():
    return list(input().split())

from collections import defaultdict
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations as p

##################################################


def main():

    """
    解説読んだ
    """
    S = input()
    N = len(S)
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            if S[i] != ")":
                dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j]) % MOD
            if (j != 0) and (S[i] != "("):
                dp[i+1][j-1] = (dp[i+1][j-1] + dp[i][j]) % MOD

    # for d in dp:
    #     print(d)
    print(dp[N][0])


    return
######################################################

if __name__ == "__main__":
    main()
