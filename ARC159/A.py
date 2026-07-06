"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < abc465?
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


def floyd(costs: list):
    N = len(costs)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                # 修正ポイント: min()関数を使わず、if文で比較する
                if costs[i][k] + costs[k][j] < costs[i][j]:
                    costs[i][j] = costs[i][k] + costs[k][j]
    return costs

##################################################


def main():

    """
    a_i,j = 1 のとき何が言えるか
    i -> j が存在し、
    i -> j+K, i -> j+2K, ... , i -> j+(K-1)K も存在する
    そいつらをコスト1としてダイクストラは書けない

    勘だけど作るグラフはN頂点で、floydの結果を用意して
    クエリをKで割った余りをその結果から見れば解けそう

    x -> y の距離はdijkstraを各頂点に対して行うことで求められるので
    その計算をあまりに対して行うだけ
    """

    N, K = i_map()
    graph = [[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(N):
        l = i_list()
        for j in range(N):
            if l[j] == 1:
                graph[i][j] = 1
    
    for g in graph:
        print(g)

    dist = floyd(graph)
    print(dist)

    Q = int(input())
    for _ in range(Q):
        s, t = i_map()
        if s == t:
            ans = 0
            continue
        s = (s-1) % N
        t = (t-1) % N
        ans = dist[s][t]
        if ans == float('inf'):
            ans = -1
        print(ans)



    return
######################################################

if __name__ == "__main__":
    main()