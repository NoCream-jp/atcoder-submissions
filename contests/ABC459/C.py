"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < give me money?
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
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations

##################################################


def main():

    """
    状態はdとcountでじゅうぶん
    y個以上の数はslから探すしかない
    """

    N, Q = i_map()
    d = [0 for _ in range(N)]
    
    count = 0
    sl = SortedList([0 for _ in range(N)])
    for _ in range(Q):
        q, c = i_map()
        
        if q == 1:
            x = c - 1
            sl.remove(d[x])
            d[x] += 1
            sl.add(d[x])
            if count < sl[0]:
                count += 1
                
        else:
            y = c
            idx = sl.bisect_left(y + count)
            ans = N - idx
            print(ans)


    return
######################################################

if __name__ == "__main__":
    main()
