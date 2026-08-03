"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < tired
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


def main():

    H, W = i_map()
    grid = [list(input()) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "T":
                ans.append((i+1, j+1))
    print(len(ans))
    for i, j in ans:
        print(i, j)
    

    return
######################################################

if __name__ == "__main__":
    main()
