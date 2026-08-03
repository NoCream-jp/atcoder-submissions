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

    H, W, Q = i_map()

    """
    対角じゃなくて(1,1)からなら逆向きに再現とかできそう
    常に左上を保持すれば簡単そう
    常に書き込める左上を保持して、書き込みと同時にずらす
    右下から常に書き込める左上までを全て書き込む、被ってたら書かない
    書いたら左上を

    と思ったけど長方形が被ると無理

    軸分けて考える。
    クエリ逆に見て、そのクエリがij独立にどこまで影響するか書く。これまでのと
    被ってれば被ってないギリまで記録する

    二次元imos
    4点に記録していく -> 無理順序関係あるし復元書けない

    左上にDFSは？
    """

    q = [tuple(input().split()) for _ in range(Q)]
    grid = [["A" for _ in range(W)] for _ in range(H)]

    visited = [[False] * W for _ in range(H)]

    for r, c, x in reversed(q):
        r = int(r) - 1
        c = int(c) - 1

        if visited[r][c]:
            continue

        # DFS
        stack = [(r, c)]
        visited[r][c] = True
        grid[r][c] = x

        while stack:
            i, j = stack.pop()

            if 0 <= i - 1 and not visited[i - 1][j]:
                visited[i - 1][j] = True
                grid[i - 1][j] = x
                stack.append((i - 1, j))

            if 0 <= j - 1 and not visited[i][j - 1]:
                visited[i][j - 1] = True
                grid[i][j - 1] = x
                stack.append((i, j - 1))

    # 出力
    for row in grid:
        print("".join(row))

    return
######################################################

if __name__ == "__main__":
    main()