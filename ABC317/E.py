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

    """
    BFS
    """

    H, W = i_map()
    grid = [list(input()) for _ in range(H)]
    start, people = (0, 0), list() # (0, 0, ">")
    # 人の位置把握
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] in [">", "<", "v", "^"]:
                people.append((i, j, grid[i][j]))

    # 目線の先に壁を構築
    DRCT = {">":(0, 1), "<":(0, -1), "v":(1, 0), "^":(-1, 0)}
    for i, j, d in people:
        grid[i][j] = "#"
        di, dj = DRCT[d]
        while 0 <= i+di <= H-1 and 0 <= j+dj <= W-1 and grid[i+di][j+dj] == ".":
            grid[i+di][j+dj] = "#"
            i += di
            j += dj
    for g in grid:
        print(g)

    # BFS
    q = deque([(start[0], start[1], 0)])
    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[start[0]][start[1]] = True
    while q:
        print(q)
        i, j, step = q.popleft()
        for di, dj in drct:
            ni, nj = i+di, j+dj
            if grid[ni][nj] == "G":
                print(step + 1)
                return
            if visited[ni][nj]:
                continue
            if 0 <= ni <= H-1 and 0 <= nj <= W-1 and not visited[ni][nj] and grid[ni][nj] != "#":
                visited[ni][nj] = True
                q.append((ni, nj, step+1))

    return
######################################################

if __name__ == "__main__":
    main()
