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
MOD = 998244353
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

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int) -> int:  # O(@N) xの所属する根
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):  # O(@N) xとyのグループを併合する
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True

    def size(self, x):  # O(@N) xのグル―プの要素数
        return -self.parents[self.find(x)]

    def same(self, x, y):  # O(@N) x, yが同じ要素に属するか
        return self.find(x) == self.find(y)

    def members(self, x):  # O(N@(N)) xが属するグループに属する要素のリスト
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):  # 全ての根の要素
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):  # O(N@(N))
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


def main():

    """
    でかいのから置いて行って、部分グラフが2から1になる瞬間の
    「使っていない辺のコストの総和」が正解

    8よりも1+2+4のほうが軽いから
    """

    N, M = i_map()
    edge = []
    for i in range(M):
        u, v = i_map()
        u -= 1
        v -= 1
        cost = i+1
        edge.append((u, v, cost))
    edge = edge[::-1]

    uf = UnionFind(N)

    parts = N

    for u, v, cost in edge:
        if parts == 2 and not uf.same(u, v):
            break
        if uf.union(u, v):
            parts -= 1
    
    ans = 0
    for u, v, cost in edge:
        if not uf.same(u, v):
            ans = (ans + pow(2, cost, MOD))%MOD

    print(ans)
######################################################

if __name__ == "__main__":
    main()
