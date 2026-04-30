"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < playing
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
from re import A
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations as p

##################################################


def main():

    for _ in range(int(input())):

        N, M, X, Y = i_map()
        X -= 1
        Y -= 1

        graph = [[] for _ in range(N)]
        for _ in range(M):
            u, v = i_map()
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)

        # DFSで経路持ちながら探索する．graph内でソートできれば，
        # 小さい順にstackに入れていけば最初に到達したものが回答

        for g in graph:
            g.sort()
        

    return
######################################################

if __name__ == "__main__":
    main()
