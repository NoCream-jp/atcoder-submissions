"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < 42222222

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


# from collections import defaultdict
# from sortedcontainers import SortedList
# from collections import deque
# import heapq
# import math
# import bisect

# from itertools import permutations as p

##################################################


def main():
    H, W = i_map()

    f = True
    grid = [input() for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if grid[i][j] == ".":
                continue
            count = 0
            if 0 <= i - 1 and grid[i - 1][j] == "#":
                count += 1
            if i + 1 < H and grid[i + 1][j] == "#":
                count += 1
            if 0 <= j - 1 and grid[i][j - 1] == "#":
                count += 1
            if j + 1 < W and grid[i][j + 1] == "#":
                count += 1
            if count == 2 or count == 4:
                continue
            else:
                f = False

    if f:
        print("Yes")
    else:
        print("No")


######################################################

if __name__ == "__main__":
    main()
