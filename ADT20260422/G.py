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
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations as p

from ABC454 import F

##################################################


def main():
    
    N, H, W = i_map()
    
    """
    2**N * HW
    """
    
    l = [list(i_map()) for i in range(N)]

    def check(grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return False
        return True

    def write(grid, si, sj, tate, yoko):
        for i in range(tate):
            for j in range(yoko):
                grid[si + tate][sj + yoko] = 1
        return

    grid = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(2<<N):

        for j in range(N):
            if (i >> j) & 1: # そのまま使う
                tate, yoko = l[j][0], l[j][1]
                for starti in range(H):
                    for startj in range(W):
            # else:
            #     tate, yoko = l[j][1], l[j][0]

                

    return
######################################################

if __name__ == "__main__":
    main()
