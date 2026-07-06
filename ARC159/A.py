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

def dijkstra(edges, num_node, start):
    node = [float('inf')] * num_node
    node[start] = 0
    node_name = []
    heapq.heappush(node_name, [0, start])
    while 0 < len(node_name):
        _, min_point = heapq.heappop(node_name)
        for factor in edges[min_point]:
            goal = factor[0]
            cost  = factor[1]
            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost
                heapq.heappush(node_name, [node[min_point] + cost, goal])
    return node

##################################################


def main():

    """
    a_i,j = 1 のとき何が言えるか
    i -> j が存在し、
    i -> j+K, i -> j+2K, ... , i -> j+(K-1)K も存在する
    そいつらをコスト1としてダイクストラは書けない

    勘だけど作るグラフはN頂点で、ダイクストラの結果を用意して
    クエリをKで割った余りをその結果から見れば解けそう

    x -> y の距離はdijkstraを二回で求められるので
    その計算をあまりに対して行うだけ
    """

    N, K = i_map()
    graph = [[] for _ in range(N)]
    rgraph = [[] for _ in range(N)]
    for i in range(N):
        l = i_list()
        for j in range(N):
            if l[j] == 1:
                graph[i].append([j, 1])
                rgraph[j].append([i, 1])
    
    for g in graph:
        print(g)

    dist = dijkstra(graph, N, 0)
    rdist = dijkstra(rgraph, N, N-1)
    print(f"{dist=}")
    print(f"{rdist=}")

    Q = int(input())
    for _ in range(Q):
        s, t = i_map()
        s -= 1
        t -= 1
        s %= K
        t %= K


    return
######################################################

if __name__ == "__main__":
    main()