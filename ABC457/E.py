"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < feel sick
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
    imosみたいに端を保存して枚数を累積
    
    idをキーに
    左を検索してそのidを持ってくる
    持ってきたすべてのidについて
    右がちょうどいいものが2個以上あるかで判定
    いるもの：
    左:idのタプルのdictionary
    id:右のタプルのdictionary
    """

    N, M = i_map()
    dct = defaultdict(list)
    for i in range(M):
        l, r = i_map()
        dct[l].append(r)

    Q = int(input())
    for q in range(Q):
        l, r = i_map()
        count = 0
        for right in dct[l]:
            if right == r:
                count += 1


    return
######################################################

if __name__ == "__main__":
    main()
