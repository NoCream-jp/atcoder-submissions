"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < too hot
"""
###################################################
# import sys
# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
# MOD = 998244353
# drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def c_list():
    return list(input().split())

from collections import defaultdict
from collections import Counter
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations

##################################################


def main():

    """
    dp[0][j] = jが晴れかつjまでの嬉しさの最大値
    dp[1][j] = jが雨かつjまでの嬉しさの最大値

    i-1もiもi+1も見る？
    手前見るだけ
    パターンがS->Rの4つある
    """
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input()
        X = i_list()
        Y = i_list()

        dp = [[0 for i in range(N+1)] for _ in range(2)] #[R], [S]

        for j in range(N):
            # j番目がR
            if S[j] == "R":
                if j == 0:
                    dp[0][j] = 0
                else:
                    dp[0][j] = max(dp[0][j-1], dp[1][j-1])
            else:
                if j == 0:
                    dp[0][j] = -X[j]
                else:
                    dp[0][j] = max(dp[0][j-1] - X[j], dp[1][j-1] - X[j])

            # j番目がS
            if S[j] == "S":
                if j == 0:
                    dp[1][j] = 0
                else:
                    dp[1][j] = max(dp[1][j-1], dp[0][j-1] + Y[j-1])
            else:
                if j == 0:
                    dp[1][j] = -X[j]
                else:
                    dp[1][j] = max(dp[1][j-1] - X[j], dp[0][j-1] - X[j] + Y[j-1])
        # for d in dp:
        #     print(d)
        # print()
        print(max(dp[0][N-1], dp[1][N-1]))


    return
######################################################

if __name__ == "__main__":
    main()