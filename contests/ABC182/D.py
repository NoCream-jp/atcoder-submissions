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
"""
各動作での最終結果と動作内での最大値を保持する
毎回、「これまでに出現した動作内での最大値」と最終結果との合計を見る
"""

def main():

    N = int(input())
    A = i_list()

    ans = 0
    now = 0 # これまでの動作の累積
    mr = 0 # 最高の結果まで動いた時のスコア
    S = 0 # 動作の最終結果
    for a in A:
        S += a
        mr = max(mr, S)
        ans = max(ans, now + mr)
        now += S
        # print(f"ans: {ans}, now: {now}, mr: {mr}, S: {S}")
    print(ans)

    return
######################################################

if __name__ == "__main__":
    main()