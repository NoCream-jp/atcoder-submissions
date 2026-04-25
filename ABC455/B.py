"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < my cat running
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
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations as p

##################################################
def check(grid, i, j, ii, jj):
    h = ii - i + 1
    for tate in range(i, i+(h + 1)//2):
        for yoko in range(j, jj+1):
            ni = i + ii - tate
            nj = j + jj - yoko
            if tate == ni and yoko == nj:
                continue
            if tate > ni or (tate == ni and yoko > nj):
                break
            if grid[tate][yoko] != grid[ni][nj]:
                return False
    return True


def main():

    H, W = i_map()
    grid = [list(input()) for _ in range(H)]
    # grid = [
    #     ["#", "#", "."],
    #     ["#", ".", "#"],
    #     ["#", "#", "#"],
    # ]

    count = 0
    for i in range(H):
        for j in range(W):
            for ii in range(i, H):
                for jj in range(j, W):
                    if check(grid, i, j, ii, jj):
                        count += 1
    print(count)


    return
######################################################

if __name__ == "__main__":
    main()