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

    """
    優先度キュー二つ
    medよりおおきい奴らがくればmedを小さいのに入れて大きいもののうち小さいものがmed
    [2]3523[5] -> 3
    [12][35] -> 2
    [122][235]
    """

    X = int(input())
    Q = int(input())

    med = X
    blst, slst = [], []
    heapq.heapify(blst) # 小さいやつらの降順
    heapq.heapify(slst) # 大きいやつらの昇順
    for _ in range(Q):
        a, b = i_map()
        if med < a and med < b:
            heapq.heappush(slst, -med)
            heapq.heappush(blst, a)
            heapq.heappush(blst, b)
            med = heapq.heappop(blst)
        elif a < med and b < med:
            heapq.heappush(slst, -a)
            heapq.heappush(slst, -b)
            heapq.heappush(blst, med)
            med = -heapq.heappop(slst)
        else:
            heapq.heappush(slst, -(min(a, b)))
            heapq.heappush(blst, max(a, b))
            med = med
        print(med)

######################################################

if __name__ == "__main__":
    main()
