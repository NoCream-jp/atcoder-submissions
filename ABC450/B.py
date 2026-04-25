"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < keep thinking
"""
###################################################

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
from re import L
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations as p

##################################################


def main():
    # ?????
    n = int(input())
    l = [[None]*(i+1) + i_list() for i in range(n-1)]
    # for a in range(n):
    #     for b in range(a+1, n):
    #         for c in range(b+1, n):
                # if l[a][b] + l[b][c] < l[a][c]:
                #     print("Yes")
                #     return
    print("No")

    return
######################################################

if __name__ == "__main__":
    main()
