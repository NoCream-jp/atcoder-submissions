"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < give me money?
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
    まず可能であるとして考える
    スロット一つだけについて、そのi番目の目aを出すことで3つの目をそろえるとき、
    単純に考えれば
    ans = max(各スロットにおけるaの最小インデックス)
    になる

    ほかに同じインデックスがあってはいけない
    """

    return
######################################################

if __name__ == "__main__":
    main()
