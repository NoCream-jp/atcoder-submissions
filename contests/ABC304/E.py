"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ <coding with atcoder library for the first time
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


# Union-Find (Disjoint Set Union)
from atcoder.dsu import DSU

# Fenwick Tree (Binary Indexed Tree)
from atcoder.fenwicktree import FenwickTree

# Segment Tree
from atcoder.segtree import SegTree

# Lazy Segment Tree
from atcoder.lazysegtree import LazySegTree

# Math (pow_mod, inv_mod, crt, floor_sumなど)
from atcoder.math import *

# Convolution (FFT)
from atcoder.convolution import convolution

# Max Flow
from atcoder.maxflow import MFGraph

# Min Cost Flow
from atcoder.mincostflow import MCFGraph

# Strongly Connected Components
from atcoder.scc import SCCGraph

# Two Satisfiability
from atcoder.twosat import TwoSAT

# String (suffix_array, lcp_array, z_algorithm)
from atcoder.string import *
from collections import defaultdict
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect

from itertools import permutations as p

##################################################


def main():
    """
    UnionFindうつだけ？
    union後外さないといけないのでダメ？

    xのrootとyのrootの組をすべて保存しておいて
    pとqのrootがそれと一致すると良くなくなる
    実際につなげる必要はないしこれでできそう

    ・xとyのrootをタプルにして集合に保存する
    ・pとqのrootのタプルが集合に
        入っていなければ良いグラフ
        入っていれば悪いグラフ


    """

    N, M = i_map()
    uf = UnionFind(N)
    for _ in range(M):
        u, v = i_map()
        u -= 1
        v -= 1
        uf.union(u, v)

    K = int(input())
    st = set()
    for _ in range(K):
        x, y = i_map()
        x -= 1
        y -= 1
        st.add((uf.find(x), uf.find(y)))
        st.add((uf.find(y), uf.find(x)))

    # print(uf)
    # 以降，グラフは良いグラフとしてよい
    Q = int(input())
    for _ in range(Q):
        p, q = i_map()
        p -= 1
        q -= 1
        tpl = (uf.find(p), uf.find(q))
        if tpl in st:
            print("No")
        else:
            print("Yes")
    return


######################################################


# 素数列挙
# 素数列挙 O(N**0.5), 空間N
def get_primes(l, r):
    if l > r or r < 2:
        return []
    l = max(2, l)
    limit = int(math.isqrt(r))
    seed_primes = []
    if limit >= 2:
        is_prime_small = [True] * (limit + 1)
        is_prime_small[0] = is_prime_small[1] = False
        for i in range(2, int(math.isqrt(limit)) + 1):
            if is_prime_small[i]:
                is_prime_small[i * i : limit + 1 : i] = [False] * len(
                    is_prime_small[i * i : limit + 1 : i]
                )
        seed_primes = [p for p, is_p in enumerate(is_prime_small) if is_p]
    n = r - l + 1
    is_prime_range = [True] * n
    for p in seed_primes:
        start = max(p * p, (l + p - 1) // p * p)
        start_idx = start - l
        if start_idx < n:
            length = (n - 1 - start_idx) // p + 1
            is_prime_range[start_idx:n:p] = [False] * length
    return [l + i for i, is_p in enumerate(is_prime_range) if is_p]


# 最大公約数
def getgcd(a, b):
    while b:
        a, b = b, a % b
    return a


# 最小公倍数
def getlcm(a, b):
    return a // getgcd(a, b) * b


# ユークリッド距離
def getdist(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# ワーシャルフロイドでO(N**3)で最短経路
# costs = [[] for _ in range(N)] の2重リスト
def floyd(costs: list, N: int):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])
    return costs


# 時計回りに回転
def rotate(grid):
    H, W = len(grid), len(grid[0])
    tmp = [["" for _ in range(W)] for __ in range(H)]
    for i in range(H):
        for j in range(W):
            tmp[i][j] = grid[H - 1 - j][i]
    return tmp


# Z-Algorithm
# 文字列の部分列
def z_algo(S):
    N = len(S)
    A = [0] * N
    i = 1
    j = 0
    A[0] = l = len(S)
    while i < l:
        while i + j < l and S[j] == S[i + j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while l - i > k < j - A[k]:
            A[i + k] = A[k]
            k += 1
        i += k
        j -= k
    return A


# 累積和
def cum_sum(l):
    a = [0 for _ in range(len(l) + 1)]
    for i in range(len(l)):
        a[i + 1] = a[i] + l[i]
    return a


def LCSof(str1, str2):
    dp = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]
    for i, vi in enumerate(str1):
        for j, vj in enumerate(str2):
            if vi == vj:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    ans = []
    i = len(str1) - 1
    j = len(str2) - 1
    while i >= 0 and j >= 0:
        if str1[i] == str2[j]:
            ans.append(str1[i])
            i -= 1
            j -= 1
        elif dp[i + 1][j + 1] == dp[i][j + 1]:
            i -= 1
        elif dp[i + 1][j + 1] == dp[i + 1][j]:
            j -= 1
    ans.reverse()
    return dp[len(str1)][len(str2)], ans


# 転倒数
def count_inversions(arr):
    """
    与えられた整数配列の転倒数（昇順に並び替えるために必要な隣接スワップの最小回数）を返す。
    :param arr: List[int]
    :return: int 転倒数
    """

    def merge_sort_and_count(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, inv_l = merge_sort_and_count(a[:mid])
        right, inv_r = merge_sort_and_count(a[mid:])
        merged = []
        i = j = inv_count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv_count += len(left) - i  # 転倒を数える
                j += 1
        merged += left[i:]
        merged += right[j:]
        return merged, inv_l + inv_r + inv_count

    _, count = merge_sort_and_count(arr)
    return count


# 素因数列挙
def prime_factors(n):
    res = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            res.append(i)
            n //= i
    if n > 1:
        res.append(n)
    return res


# [me, comp] -> winner index
def janken(l):
    a, b = l
    d = {"G": 0, "C": 1, "P": 2}
    n = (d[a] - d[b]) % 3
    if n == 0:
        return 2  # あいこ
    elif n == 1:
        return 1  # 右
    else:
        return 0  # 左


# 辞書作るだけ
# {名前: その数}
def mkdct(l):
    d = {}
    for n in l:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    return d


def lis(seq):
    LIS = [seq[0]]
    for i in range(len(seq)):
        if seq[i] > LIS[-1]:
            LIS.append(seq[i])
        else:
            LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]
    return LIS, len(LIS)


def my_bisect_left(a, x):
    if x < a[0]:
        return None
    if a[-1] < x:
        return None
    return bisect.bisect_left(a, x)


def my_bisect_right(a, x):
    if x < a[0]:
        return None
    if a[-1] < x:
        return None
    return bisect.bisect_right(a, x)


# ローリングハッシュクラス
class RollingHash:
    def __init__(self, S, b=3491, m=999999937):
        """任意の基数と法でハッシュを生成する"""
        n = len(S)
        self.prefix = prefix = [0] * (n + 1)
        self.power = power = [1] * (n + 1)
        self.b = b
        self.m = m
        for i in range(n):
            c = ord(S[i])
            prefix[i + 1] = (prefix[i] * b + c) % m
            power[i + 1] = (power[i] * b) % m

    def get(self, l, r):
        """S[l, r) のハッシュを求める"""
        return (self.prefix[r] - self.power[r - l] * self.prefix[l]) % self.m

    def concat(self, h1, h2, l2):
        """S1+S2 のハッシュを、それぞれのハッシュから求める"""
        return (self.power[l2] * h1 + h2) % self.m

    def lcp(self, l1, r1, l2, r2):
        """S[l1, r1) とS[l2, r2) の最大共通接頭辞を求める"""
        # LCPの最小値 (範囲内)
        low = 0
        # LCPの最大値 + 1 (範囲外)
        high = min(r1 - l1, r2 - l2) + 1
        while high - low > 1:
            mid = (high + low) // 2
            if self.get(l1, l1 + mid) == self.get(l2, l2 + mid):
                low = mid
            else:
                high = mid
        return low


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


#########################################################################

if __name__ == "__main__":
    main()
