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

# 累積和 総和 = (r+1番目) - (l番目)
def cum_sum(l):
    a = [0 for _ in range(len(l) + 1)]
    for i in range(len(l)):
        a[i + 1] = a[i] + l[i]
    return a

def main():

    N, M, P = i_map()
    A = i_list()
    B = i_list()

    A.sort()
    B.sort()

    cumA = cum_sum(A)
    cumB = cum_sum(B)
    
    """
    二分探索で見つけたインデックスまで累積和でもとめる
    右側はP*残りの数
    """
    
    ans = 0
    for a in A:
        idx = bisect.bisect_right(B, P - a - 1)
        ans += cumB[idx] + a*idx
        ans += (M - idx) * P
    print(ans)

    return
######################################################

if __name__ == "__main__":
    main()
