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

    H, W = i_map()
    grid = [list(input()) for _ in range(H)]

    a, b, c, d = 0, 0, H-1, W-1

    while True:
        changed = False

        # 上
        f = True
        for j in range(b, d + 1):
            if grid[a][j] == "#":
                f = False
                break
        if f and a <= c:
            a += 1
            changed = True

        # 下
        f = True
        for j in range(b, d + 1):
            if grid[c][j] == "#":
                f = False
                break
        if f and a <= c:
            c -= 1
            changed = True

        # 左
        f = True
        for i in range(a, c + 1):
            if grid[i][b] == "#":
                f = False
                break
        if f and b <= d:
            b += 1
            changed = True

        # 右
        f = True
        for i in range(a, c + 1):
            if grid[i][d] == "#":
                f = False
                break
        if f and b <= d:
            d -= 1
            changed = True

        if not changed:
            break

    for i in range(a, c + 1):
        for j in range(b, d + 1):
            print(grid[i][j], end="")
        print()


    return
######################################################

if __name__ == "__main__":
    main()