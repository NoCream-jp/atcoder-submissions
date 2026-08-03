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

    """
    全部真ん中できるのが最善
    Kが大きすぎる
    が、全てが2を下回った時点で答えは1になる。
    から、Nlog(maxA)でできそう

    heapqで限界までシミュレーションできる？
    """
    N, K = i_map()
    l = map(float, i_list())
    q = [-n for n in l]
    heapq.heapify(q)

    while K:
        K -= 1
        top = -heapq.heappop(q)
        if top <= 1:
            break
        else:
            nxt = top / 2
            nxt *= -1
            heapq.heappush(q, nxt)
            heapq.heappush(q, nxt)
        # print(q)
    print(sorted(q))
    print((-heapq.heappop(q) + 1))
    

    return
######################################################

if __name__ == "__main__":
    main()