"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗   < i hate 350p problems..
                    ████╝

"""


######################################################


def main():
    """
    避ければいい
    いけるの全部たして，1111...かどうか？でよくないか
    01111と
    10000だけがいけても，
    01111を作るときに毒を踏む？
    1111(15) -> 1101(11) -> 1001(9) -> 1000(1)みたいに
    一つ違いで立ってるのが1の数字まで戻れるかどうか
    ↑違う．

    2の倍数を足していくDPで追うのは無理，N^2
    各ビットごとに次におけるビットを保存するのもあり
    1つずつしか置けないから，次の安全な状態がつながってればいい
    1001 -> 1101 がokとするの，すごくやりにくい
    ↑つながりを計算できん

    bit_count毎にわけて全種類あればOK,ではない．
    到達不可能な組もあるから
    111100 -> 101111とか1手で行けない

    1(10) = 1000(2)（N=4のとき） から見て
    ・1100
    ・1010
    ・1001 があるかどうか
    はN-1回で見れる．
    それぞれの数からごり押し計算できる？各数について高々18回
    2^(5^15)になるからそれぞれの数字を見るのは無理．やっぱbitごとに見るDPじゃない？
    """

    T = int(input())
    for t in range(T):
        N = int(input())
        S = input()

        num = 0
        for i in range(N):
            print("wakaran")


######################################################


# 入力
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
# drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# drct = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
# NUM = 998244353
def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def c_list():
    return list(input().split())


# import sys
# sys.setrecursionlimit(10 ** 6)
# import math
import heapq

# import numpy as np
# import bisect as bs
# from collections import deque
# from itertools import permutations
# from itertools import combinations as cmb
from collections import defaultdict
# from sortedcontainers import SortedList


class Mylib:
    # 探す値以下の要素がある最大インデックス
    def bisect_left(self, a, x, lo=0, hi=None):
        if hi is None:
            hi = len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    # 探す値以上の要素がある最小インデックス
    def bisect_right(self, a, x, lo=0, hi=None):
        if hi is None:
            hi = len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if x < a[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def find_rightmost_index(self, a, x):
        i = self.bisect_right(a, x)
        if i > 0 and a[i - 1] == x:
            return i - 1
        else:
            return -1

    # 最大公約数
    def getgcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    # 最小公倍数
    def getlcm(self, a, b):
        return a // Mylib().getgcd(a, b) * b

    # ユークリッド距離
    def getdist(self, x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    # ワーシャルフロイドでO(N**3)で最短経路
    # costs = [[] for _ in range(N)] の2重リスト
    def floyd(self, costs: list, N: int):
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])
        return costs

    # 時計回りに回転
    def rotate(self, grid):
        H, W = len(grid), len(grid[0])
        tmp = [["" for _ in range(W)] for __ in range(H)]
        for i in range(H):
            for j in range(W):
                tmp[i][j] = grid[H - 1 - j][i]
        return tmp

    # Z-Algorithm
    # 文字列の部分列
    def z_algo(self, S):
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
    def cum_sum(self, l: list):
        a = [0 for _ in range(len(l) + 1)]
        for i in range(1, len(l) + 1):
            a[i] = a[i - 1] + l[i - 1]
        return a

    def LCSof(self, str1, str2):
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
    def count_inversions(self, arr):
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

    def prime_factors(self, n):
        res = []
        for i in range(2, int(n**0.5) + 1):
            while n % i == 0:
                res.append(i)
                n //= i
        if n > 1:
            res.append(n)
        return res

    # [me, comp] -> winner index
    def janken(self, l):
        a, b = l
        d = {"G": 0, "C": 1, "P": 2}
        n = (d[a] - d[b]) % 3
        if n == 0:
            return 2  # あいこ
        elif n == 1:
            return 1  # 右
        else:
            return 0  # 左

    def mkdic(self, l: list):
        d = {}
        for n in l:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        return d

    # ダイクストラ
    def dijkstra(self, edges, num_node):
        node = [float("inf")] * num_node  # スタート地点からの最小コスト
        node[0] = 0
        node_name = []
        heapq.heappush(node_name, [0, 0])
        while 0 < len(node_name):
            _, min_point = heapq.heappop(node_name)  # min_point:
            for goal, cost in edges[min_point]:
                if node[min_point] + cost < node[goal]:
                    node[goal] = node[min_point] + cost
                    heapq.heappush(node_name, [node[min_point] + cost, goal])
        return node

    def RLE(self, l: list) -> list:
        ans = []
        tmp = ""
        count = 1
        for i in range(len(l)):
            if l[i] != tmp:
                if tmp != (""):
                    ans.append((tmp, count))
                tmp = l[i]
                count = 1
            else:
                count += 1
        if tmp != "":
            ans.append((tmp, count))
        return ans

    # O(N)素因数分解
    def factorization(n) -> list:
        arr = []
        tmp = n
        for i in range(2, int(-(-(n**0.5) // 1)) + 1):
            if tmp % i == 0:
                cnt = 0
                while tmp % i == 0:
                    cnt += 1
                    tmp //= i
                arr.append([i, cnt])
        if tmp != 1:
            arr.append([tmp, 1])
        if arr == []:
            arr.append(n, 1)
        return arr

    # 素数列挙
    def SOE(x):
        nums = [i for i in range((x + 1))]
        for i in range(2, int(pow(x, 0.5))):
            if nums[i] != 0:
                for j in range(i, x + 1):
                    if x + 1 <= i * j:
                        break
                    nums[i * j] = 0
        primes = set(nums)
        return primes

    # 基数変換
    # 文字列から文字列
    # O(N)
    def base_change(s: str, srcn: int, distn: int) -> str:
        n = 0  # 元の数(10)
        i = 0  # 何乗か
        for c in s:
            c = int(c)
            n += c * (srcn**i)
        print(f"元の数(10) : {n}")

        i = 0  # 何乗か
        dist = 0
        while n:
            dist += (n % distn) * (distn**i)
            i += 1
            n //= srcn
        return str(dist)


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


# 入力
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
# drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# drct = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
# NUM = 998244353
def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def c_list():
    return list(input().split())


# import math
import heapq

# import sys
# sys.setrecursionlimit(10 ** 6)
# import numpy as np
# import bisect as bs
from collections import deque

# from itertools import permutations
# from itertools import combinations as cmb
from collections import defaultdict
# from sortedcontainers import SortedList


if __name__ == "__main__":
    main()
