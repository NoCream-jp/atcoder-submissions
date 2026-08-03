"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < keep thinking
"""
###################################################

# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
# MOD = 998244353
drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


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

    # 多始点したいけど1000 * 1000でDFSできそう
    # 四方だけみてUnionFindのほうが楽かも
    # 白をUnionして，端を含まない群の数が解答
    # i*W + j
    # root毎に見直してもHWしかかからない
    # 端または#が入ったらそのrootはダメ
    H, W = i_map()
    grid = [list(input()) for _ in range(H)]
    uf = UnionFind(H*W)

    st = set() # ダメなrootが入る
    for i in range(H):
        for j in range(W):
            num = i*W+j
            if grid[i][j] == "#":
                continue
            for di, dj in drct:
                ni, nj = i+di, j+dj
                if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == ".":
                    nxtnum = ni*W+nj
                    uf.union(num, nxtnum)
    ans = uf.group_count()

    for i in range(H):
        for j in range(W):
            num = i*W+j

            if grid[i][j] == "#" or not check(num, H, W):
                st.add(uf.find(num))
    
    print(ans-len(st))
    
            

    return
######################################################
def check(num, H, W):
    if 0 <= num < W or (H-1)*W <= num < H*W:
        return False
    elif num % W == 0 or num % W == W-1:
        return False
    return True


# Union-Findクラス
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

if __name__ == "__main__":
    main()
