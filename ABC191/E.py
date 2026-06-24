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
    多始点？
    """

    N, M = i_map()
    graph = [defaultdict(int) for _ in range(N)]
    # i->jで最も軽い辺のみ採用するために辞書にする
    for _ in range(M):
        a, b, c = i_map()
        a -= 1
        b -= 1
        if graph[a][b]:
            graph[a][b] = min(graph[a][b], c)
        else:
            graph[a][b] = c
    
    zero = [False for _ in range(N)]
    ans = [-1 for _ in range(N)]
    for start in range(N):
        # BFS
        visited = zero.copy()
        q = deque()
        q.append((start, 0))
        loop = True
        while q and loop:
            now, cost = q.popleft()
            if visited[now]:
                continue
            visited[now] = True
            for nxt in graph[now]:
                nxtcost = graph[now][nxt]
                if nxt == start:
                    ans[start] = cost + nxtcost
                    loop = False
                    break
                if not visited[nxt]:
                    q.append((nxt, cost + nxtcost))
    
    for a in ans:
        print(a)
            

    return
######################################################

if __name__ == "__main__":
    main()