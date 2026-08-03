"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < wanna solve green
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
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations as p

##################################################


def main():

    """
    di = (Yi - Xi)//2 + 1（0にならない制約上、必ず差が出る）
    として
    diが正なら飛ばす
    diが負ならメモする。
    またZの総数と現在正だったiから「ほしいZの値」が分かる。
    
    メモしたi全てを見て以下を解く
    数列Zとd
    スコアZiを得るためのコストがdiのとき、
    総スコアを「ほしいZの値」以上にするための最小のコストの総和は？
    """

    N = int(input())
    l = [] # (値、コスト) 
    allZ = 0 # ほしいZの値の計算に使う
    for i in range(N):
        x, y, z = i_map()
        allZ += z
        if y < x:
            continue
        cost = (y - x) // 2 + 1
        l.append((z, cost))
    Z = [l[i][0] for i in range(len(l))]
    C = [l[i][1] for i in range(len(l))]
    # print("Z", Z)
    # print("C", C)

    # ほしいZの値の計算
    goal = (allZ + 1) // 2
    loseZ = sum(Z)
    getZ = allZ - loseZ
    # print(f"goal={goal}, loseZ={loseZ}, getZ={getZ}")
    if goal <= getZ:
        print(0)
        return
    goal -= getZ

    """
    dp
    N * sum(Z_i)
    dp[i][j]:
    i番目まで見たときにZ値の総和jを達成するために必要な最小コスト
    value, cost = l[i][0], l[i][1]
    dp[i][j] = min(dp[i - 1][j -  value] + cost, dp[i - 1][j])
    """
    INF = float('inf')
    max_Z = sum(Z)
    dp = [[INF for _ in range(max_Z + 1)] for _ in range(len(Z) + 1)]
    dp[0][0] = 0

    for i in range(len(Z)):
        value, cost = Z[i], C[i]
        for j in range(max_Z + 1):
            dp[i + 1][j] = dp[i][j]
            if j - value >= 0:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - value] + cost)
    ans = min(dp[-1][goal:])
    print(ans)
    


    return
######################################################

if __name__ == "__main__":
    main()
