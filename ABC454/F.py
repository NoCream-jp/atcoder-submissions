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

##################################################


def main():
    
    N, M = i_map()
    w = [0 for _ in range(N+1)]
    for _ in range(M):
        l, r = i_map()
        l -= 1
        r -= 1
        w[l] += 1
        w[r+1] -= 1

    wall = [0 for i in range(N)]
    tmp = 0
    for i in range(N):
        wall[i] = tmp + w[i]
        tmp = wall[i]

    ans = min(wall)
    print(ans)
    

    return
######################################################

if __name__ == "__main__":
    main()
