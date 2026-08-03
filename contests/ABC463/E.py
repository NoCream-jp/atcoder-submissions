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
    全部に張らずにもう一つ作って経由するだけ
    ダイクストラなら全部一気に出せる
    """

    N, M, Y = i_map()
    
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u, v, c = i_map()
        u -= 1
        v -= 1
        graph[u].append((v, c))
        graph[v].append((u, c))
        
    X = i_list()

    n = N
    for i in range(N):
        graph[i].append((n, X[i] + Y))
        graph[n].append((i, X[i]))
    
    # dijkstra
    dist = [float("inf") for _ in range(N+1)]
    start = 0
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if dist[u] < d:
            continue
        for v, cost in graph[u]:
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                heapq.heappush(pq, (dist[v], v))
    
    for i in range(1, N):
        print(dist[i], end=" ")

    return
######################################################

if __name__ == "__main__":
    main()
