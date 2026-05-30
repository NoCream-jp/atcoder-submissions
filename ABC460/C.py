"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < give me higher rate point !!!!
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
from itertools import permutations

##################################################


def main():

    """
    ソート
    ネタ昇順、シャリ昇順で
    小さいネタで使えなかったものはもう使えないので
    """

    N, M = i_map()
    A = i_list() # し
    B = i_list() # ね
    A.sort()
    B.sort()

    count = 0
    aidx, bidx = 0, 0
    while aidx <= N-1 and bidx <= M-1:
        if B[bidx] <= A[aidx] * 2:
            count += 1
            aidx += 1
            bidx += 1
        else:
            aidx += 1
    print(count)

    return
######################################################

if __name__ == "__main__":
    main()
