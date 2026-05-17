"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < difficult?
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
    ans = [[0 for _ in range(W)] for _ in range(H)]
    if H == 1:
        if W == 1:
            print(0)
            return
        for j in range(W):
            if j == 0 or j == W-1:
                ans[0][j] = 1
            else:
                ans[0][j] = 2
    elif W == 1:
        for i in range(H):
            if i == 0 or i == H-1:
                ans[i][0] = 1
            else:
                ans[i][0] = 2
    else:
        kado = {(0, 0), (0, W-1), (H-1, 0), (H-1, W-1)}
        for i in range(H):
            for j in range(W):
                if (i, j) in kado:
                    ans[i][j] = 2
                elif i == 0 or i == H-1 or j == 0 or j == W-1:
                    ans[i][j] = 3
                else:
                    ans[i][j] = 4

    for i in range(H):
        print(*ans[i])

    return
######################################################

if __name__ == "__main__":
    main()
