"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < midnight coding
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
    dpに見える
    dp[i]はi枚目まで見たときに条件を満たせるように裏返しするパターンの最大数
    dp[0] = 2

    と思ったけどi時点での登場カードの種類を持たないと無理そう
    dpを2次元にするとそれも持てるけどメモリがN^2で足りなさそう
    
    """

    return
######################################################

if __name__ == "__main__":
    main()