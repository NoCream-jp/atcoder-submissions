"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗   <  !!!
                    ████╝

"""

###################################################
# 入力
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

# from sortedcontainers import SortedList
from collections import deque
# import heapq
# import math
# import bisect

# from itertools import permutations as p

##################################################


def main():
    H, W = i_map()
    A = [list(input()) for _ in range(H)]
    B = [["" for _ in range(W)] for _ in range(H)]
    for i in range(H):  # 反転バージョンをBに作成
        for j in range(W):
            if A[i][j] == "o":
                B[i][j] = "x"
            elif A[i][j] == "x":
                B[i][j] = "o"
            else:
                B[i][j] = A[i][j]

    grid = [A, B]

    """
    ?を踏むとA⇔Bで入れ替わるようにして幅優先探索
    """
    start = [0, 0]
    goal = [0, 0]
    for i in range(H):
        for j in range(W):
            if A[i][j] == "S":
                start = [i, j]
            elif A[i][j] == "G":
                goal = [i, j]

    q = deque((start[0], start[1], 0))
    while q:
        y, x, cost = q.pop()
        for dy, dx in drct:
            ny, nx = y + dy, x + dx


######################################################

if __name__ == "__main__":
    main()
