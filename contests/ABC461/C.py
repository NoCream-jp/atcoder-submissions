"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < give me higher rate point !!!!
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
    貪欲に
    M種類までは各種類のうち最大のものを取ってくる
    そのあとは全てで見る
    種類ごとにソート、全部でソート？
    種類毎にリストを作って、最大と色のタプルを作っておく。
    それとは別にもう一つ全てのリストを入れたslを作る。
    M回ののうちは、選んだものを削除する。
    """

    N, K, M = i_map()
    DIFF = K - M
    d = defaultdict(list)
    for _ in range(N):
        c, v = i_map()
        d[c].append(v)

    lst = []
    for k in d:
        d[k].sort()
        lst.append((k, d[k][-1])) # (color, score)
    # print("lst", lst)
    lst.sort(key=lambda x:x[-1])

    ans = 0
    # まずはM回種類をまたいで最大値
    while M:
        M -= 1
        color, score = lst.pop()
        ans += score
        d[color].pop()
    # 次に残り物を混ぜてソート
    l = []
    for k in d:
        for v in d[k]:
            l.append(v)
    l.sort()
    for _ in range(DIFF):
        ans += l.pop()
    
    print(ans)

    

    return
######################################################

if __name__ == "__main__":
    main()
