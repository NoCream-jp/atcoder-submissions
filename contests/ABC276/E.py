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
# from typing import _ReturnT_nd_co
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import filterfalse, permutations as p

##################################################


def main():

    """
    SのまわりからBFS
    """

    H, W = i_map()
    grid = [list(input()) for _ in range(H)]
    si, sj = 0, 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "S":
                si, sj = i, j
    
    q = deque([])
    label = 1
    for di, dj in drct:
        if 0 <= si+di <= H-1 and 0 <= sj+dj <= W-1 and grid[si+di][sj+dj] == ".":
            q.append((si+di, sj+dj, label)) # この値どうしを突き合わせて4以上なら
            label += 1
    if len(q) < 2:
        print("No")
        return
    
    di, dj = 0, 0
    # BFS
    ### 追加前に判定する
    visited = [[-1 for _ in range(W)] for _ in range(H)]
    visited[si][sj] = -1
    while q:
        i, j, label = q.popleft()
        if visited[i][j] == label:
            continue
        visited[i][j] = label
        for di, dj in drct:
            ni, nj = i+di, j+dj
            if 0 <= ni <= H-1 and 0 <= nj <= W-1 and grid[ni][nj] == ".":
                if visited[ni][nj] != -1 and visited[ni][nj] != label: # 4以上かつ自分じゃないとき
                    print(f"Yes")
                    return
                if visited[ni][nj] == -1 and visited[ni][nj] != label:
                    q.append((ni, nj, label))

    # for v in visited:
    #     print(v)        

    print("No")
    return
######################################################

if __name__ == "__main__":
    main()
