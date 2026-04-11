"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝

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

# from sortedcontainers import SortedList
from collections import deque

# import heapq
# import math
import bisect

from itertools import permutations as p

##################################################


def main():
    """
    Xのとき、
    A_iより左ならば、すべての色がB_i下にずれる
    A_iより右ならば、すべての色がB_i上にずれる

    Yのとき、
    A_iより下ならば、B_i左にずれる
    A_iより上ならば、B_i右にずれる

    シミュレーションは絶対無理
    ずらすって操作だけなら片方無視してみたりできるけど
    大きすぎてシミュレーションできない

    黒マスの数は変わらない

    切り離されてしまう回数は最大14回、毎回たかだか2分割なので
    最悪の場合領域が2**14個(よりは小さいけど)になる。
    長方形領域を対角の2点で表現すれば、管理できるし数も保持できる
    分割していくことはできそう

    連結成分を最後に数えるのにはO(2**N(リスト全部触るだけ))よりも、
    UnionFindでunion()するぶんもうすこしかかる
    """
    # print(2**14)

    N, X, Y = i_map()
    l = [((0, 0), (X - 1, Y - 1))]  # 黒い領域がどこからどこまでか([, ])
    q = deque(l)
    for i in range(N):
        c, a, b = input().split()
        a, b = int(a), int(b)
        if c == "X":  # A_iより左なら下に、右なら上にずれる
            loop = len(q)
            while loop:
                loop -= 1
                tmp = q.popleft()
                # 必ずx1が左、x2が右
                x1, y1, x2, y2 = tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1]
                if x2 < a:  # 全部左の場合、bだけ下にずれる
                    q.append(((x1, y1 - b), (x2, y2 - b)))
                elif a < x1:  # 全部右の場合、bだけ上にずれる
                    q.append(((x1, y1 + b), (x2, y2 + b)))
                else:  # 分割されてしまう場合
                    q.append(((x1, y1 - b), (a - 1, y2 - b)))  # 左側を保存
                    q.append(((a, y1 + b), (x2, y2 + b)))  # 右側を保存
        else:  # A_iより下なら左に、上なら右にずれる
            loop = len(q)
            while loop:
                loop -= 1
                tmp = q.popleft()
                # 必ずy1が上、y2が下
                x1, y1, x2, y2 = tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1]
                if y2 < a:  # 全部下の場合、bぶん左にずれる
                    # print("全部左")
                    q.append(((x1 - b, y1), (x2 - b, y2)))
                elif a < y1:  # 全部上の場合、bぶん右にずれる
                    # print("全部右")
                    q.append(((x1 + b, y1), (x2 + b, y2)))
                else:  # 分割されてしまう場合
                    # print("分割")
                    q.append(((x1 - b, y1), (x2 - b, a - 1)))  # 下側を保存
                    q.append(((x1 + b, a), (x2 + b, y2)))  # 上側を保存

    # print(q)
    # えらすぎ、がんばった

    """
    連結成分を数える。隣接してるかどうかの判定は関数書きたいけど
    N**2になるのが大きすぎる？
    n**14**2
    最後に数えるのは14回とそのソートでいいからいいとして
    いや、連結してる可能性があるのはソートしたときに左右だけ。
    領域が固有になって重なるわけがない処理をしてるから、
    近くしか隣接しない
    ので一応縦横の2回はソートしないといけないが、線形時間でできる
    """

    lst = list(q)
    for i in range(len(lst)):
        a, b = lst[i]
        lst[i] = (a, b, i)

    uf = UnionFind(len(lst))

    for i in range(len(lst) - 1):
        x1a, y1a, x2a, y2a = lst[i][0][0], lst[i][0][1], lst[i][1][0], lst[i][1][1]
        number1 = lst[i][2]
        for j in range(i + 1, len(lst)):
            x1b, y1b, x2b, y2b = (
                lst[j][0][0],
                lst[j][0][1],
                lst[i + 1][1][0],
                lst[i + 1][1][1],
            )
            number2 = lst[j][2]
            if max(x1a, x1b) <= min(x2a, x2b):
                if y2a + 1 == y1b:
                    uf.union(number1, number2)
            if max(y1a, y1b) <= min(y2a, y2b):
                if x2a + 1 == x1b:
                    uf.union(number1, number2)

    lst.sort(key=lambda x: x[2])  # number順にして数えられるようにする

    def calc(x1, y1, x2, y2):
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        return width * height

    roots = uf.roots()
    print(len(roots))
    ansl = []
    for r in roots:
        members = uf.members(r)
        # print("members", members)
        # print(members)
        ans = 0
        for m in members:
            x1, y1 = lst[m][0]
            x2, y2 = lst[m][1]
            ans += calc(x1, y1, x2, y2)
        ansl.append(ans)

    ansl.sort()
    print(*ansl)
    return


######################################################


# 素数列挙
def sieve(n):
    primes = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime and i > 1]


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
    a = [0 for _ in range(len(l))]
    a[0] = l[0]
    for i in range(1, len(l)):
        a[i] = a[i - 1] + l[i]
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
def mkdic(l):
    d = {}
    for n in l:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    return d


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
