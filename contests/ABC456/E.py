"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < tired
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
from typing import _ReturnT_nd_co
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations as p

##################################################


def main():

    """
    毎回「隣接していてかつ次の日が休日であるノードのみに到達できる」としてDFSする、ループができたら終わり
    10倍にすればいい
    """

    T = int(input())
    for t in range(T):
        N, M = i_map()
        graph = [[] for _ in range(N)]
        for i in range(M):
            u, v = i_map()
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)
        W = int(input())
        S = [input() for _ in range(N)]
        print(graph, S)

        stack = [(0, 0)] # ノード、到達した日
        visited = [False for _ in range(N)]
        visited[0] = True
        while stack:
            now, today = stack.pop()
            tommorow = (today + 1) % W
            for nxt in graph[now]:
                if S[nxt][tommorow] == "o":
                    if visited[nxt] == True:
                        print("Yes")
                        return
                    stack.append((nxt, tommorow))
            visited[now] = True
        print("No")

    return
######################################################

if __name__ == "__main__":
    main()
