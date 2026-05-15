"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < difficult 
"""
###################################################

# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
# MOD = 998244353
drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


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
    grid = [input() for _ in range(H)]

    snuke = "snuke"
    start = (0, 0, 0) # i, j, idx
    
    stack = [start]
    visited = [[False for j in range(W)] for i in range(H)]
    visited[0][0] = True
    while stack:
        i, j, idx = stack.pop()
        if i == H-1 and j == W-1:
            print("Yes")
            return
        for di, dj in drct:
            ni, nj = i + di, j + dj
            nidx = (idx + 1) % 5
            if 0 <= ni < H and 0 <= nj < W:
                if grid[ni][nj] == snuke[nidx] and not visited[ni][nj]:
                    stack.append((ni, nj, nidx))
                    visited[ni][nj] = True
                else:
                    continue
    print("No")

    return

######################################################

if __name__ == "__main__":
    main()
