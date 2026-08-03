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

    l = i_list()
    ABC = l[:3]
    DEF = l[3:]
    ans1 = 1
    for n in ABC:
        ans1 = (ans1 * n) % MOD
    ans2 = 1
    for n in DEF:
        ans2 = (ans2 * n) % MOD
    print((ans1 - ans2) % MOD) 

    return
######################################################

if __name__ == "__main__":
    main()
