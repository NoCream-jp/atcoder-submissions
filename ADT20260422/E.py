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

    """
    mnまではなぞる
    mn更新すれば，全部でNしか触らなくていい
    """
    
    N, Q = i_map()

    pc = [1 for i in range(N+1)]
    mn = 1  
    for q in range(Q):
        x, y = i_map()
        ans = 0
        while mn <= x:
            ans += pc[mn]
            pc[y] += pc[mn]
            mn += 1
        print(ans)
    return
######################################################

if __name__ == "__main__":
    main()
