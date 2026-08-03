###################################################
# import sys
# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
# MOD = 998244353
# drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = float('inf')

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
def dijkstra(start, graph, N):
    dist = [INF] * N
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cost, now = heapq.heappop(pq)
        if cost > dist[now]:
            continue
        for nxt, nxtcost in graph[now]:
            if dist[nxt] > cost + nxtcost:
                dist[nxt] = cost + nxtcost
                heapq.heappush(pq, (dist[nxt], nxt))
    return dist

def main():
    N, M = i_map()
    graph = [[] for _ in range(N)]
    r_graph = [[] for _ in range(N)]

    self_loop = [float('inf')] * N

    for _ in range(M):
        a, b, c = i_map()
        a -= 1
        b -= 1
        graph[a].append((b, c))
        r_graph[b].append((a, c))
        if a == b:
            self_loop[a] = min(self_loop[a], c)

    for i in range(N):
        dist = dijkstra(i, graph, N)
        r_dist = dijkstra(i, r_graph, N)

        ans = self_loop[i]

        for j in range(N):
            if j == i:
                continue
            if dist[j] != INF and r_dist[j] != INF:
                ans = min(ans, dist[j] + r_dist[j])
    
        print(ans if ans != INF else -1)
######################################################

if __name__ == "__main__":
    main()