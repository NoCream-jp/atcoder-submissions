"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗   <  !!!
                    ████╝

"""

###################################################
# 入力
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
# from sortedcontainers import SortedList
# from collections import deque
# import heapq
# import math
# import bisect

# from itertools import permutations as p

##################################################


def main():
    """
    ufの根が黒に属するかどうかと，その頂点集合の中の黒の数で判断
    根をキーに辞書をつくって黒の数を見ればいい
    他に今どの色かのリストも要る．辞書になかった場合自分の色を教える必要がある
    1. unionするときに同じ木でなければ黒カウントを合算するが辞書に無い場合自分の色に応じて合算に加える
    2. 自分の根を辞書から探して情報を追加する,なければ
    3. 辞書[v]が0でないかどうか見ればよい
    辞書に0をN個並べておけば楽だが根が変わった後は変更できないのでだめ
    """
    N, Q = i_map()
    uf = UnionFind(N)

    d = {}  # 黒頂点の根のマップ
    color = [0 for _ in range(N)]  # 白0

    for _ in range(Q):
        q = i_list()
        t = q[0]
        if t == 1:
            u, v = q[1] - 1, q[2] - 1
            if uf.same(u, v):
                pass
            else:
                uroot, vroot = uf.find(u), uf.find(v)
                if uroot not in d:
                    if vroot not in d:  # どちらもない
                        uf.union(u, v)
                        d[uf.find(u)] = color[u] + color[v]
                    else:  # uだけない
                        vcount = d[uf.find(v)]
                        uf.union(u, v)
                        d[uf.find(u)] = vcount + color[u]
                elif vroot not in d:  # vだけない
                    ucount = d[uf.find(u)]
                    uf.union(u, v)
                    d[uf.find(u)] = ucount + color[v]
                else:  # どちらもある
                    ucount, vcount = d[uf.find(u)], d[uf.find(v)]
                    uf.union(u, v)
                    d[uf.find(u)] = ucount + vcount

        elif t == 2:
            v = q[1] - 1
            root = uf.find(v)
            if root in d:
                if color[v] == 0:
                    d[root] += 1
                else:
                    d[root] -= 1
            else:
                if color[v] == 0:
                    d[root] = 1  # 黒になった
                else:
                    d[root] = 0  # 白になった
            color[v] = int(not (color[v]))
        else:
            v = q[1] - 1
            root = uf.find(v)
            if root in d and d[root] != 0:
                print("Yes")
            else:
                print("No")


######################################################


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


##################################################

if __name__ == "__main__":
    main()
