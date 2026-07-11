"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < unbelievable
"""
###################################################
# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
# MOD = 998244353
# drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# drct_char = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

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

#########################################################################
# main
#########################################################################

    
def main():

    """
    A[i]の

    i ~ jのaverage

    ( ps(A[i]) - ps(A[j]) ) / ( i - j + 1) = K

    ( ps(A[i]) - ps(A[j]) ) = K ( i - j + 1 ) = Ki - Kj + K

    ps(A[i]) - Ki = ps(A[j]) - Kj + K

    
    
    """

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    keys = []
    vals = []

    import bisect

    ps = 0
    ans = 0

    for j in range(n):
        # まだ a[j] を足していないので、ps は S_{j-1} の状態
        left_value = ps - k * (j - 1)

        pos = bisect.bisect_left(keys, left_value)
        if pos == len(keys):
            keys.append(left_value)
            vals.append(j)

        # a[j] を足すことで、ps は S_j になる
        ps += a[j]

        # 数式の S_j - K * j
        right_value = ps - k * j
        
        # 右端 j に対して、条件を満たす最も左の i を探す
        pos = bisect.bisect_left(keys, right_value)

        if pos == len(keys):
            continue

        # j - i + 1 で区間の長さを計算し、最大値を更新
        ans = max(ans, j - vals[pos] + 1)

    return


#########################################################################
# Classes
#########################################################################

class PrefixSum2D:
    def __init__(self, grid):
        """
        二次元配列（グリッド）を受け取り、二次元累積和を構築する
        :param grid: 2次元リスト (H x W)
        """
        self.H = len(grid)
        self.W = len(grid[0]) if self.H > 0 else 0
        
        # 1-indexedの累積和テーブル (H+1 x W+1) を0で初期化
        self.S = [[0] * (self.W + 1) for _ in range(self.H + 1)]
        
        # 累積和の構築
        for i in range(self.H):
            for j in range(self.W):
                self.S[i+1][j+1] = (grid[i][j] 
                                  + self.S[i][j+1] 
                                  + self.S[i+1][j] 
                                  - self.S[i][j])

    def query(self, r1, c1, r2, c2):
        """
        左上 (r1, c1) から 右下 (r2, c2) までの矩形領域の要素の和
        """
        # 無効な範囲が指定された場合は0を返す
        if r1 > r2 or c1 > c2:
            return 0
        r1 = max(0, r1)
        c1 = max(0, c1)
        r2 = min(self.H - 1, r2)
        c2 = min(self.W - 1, c2)

        # 包除原理を用いてO(1)で和を計算
        return (self.S[r2+1][c2+1]
              - self.S[r1][c2+1]
              - self.S[r2+1][c1]
              + self.S[r1][c1])

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

    def get(self, left, right):
        """S[l, r) のハッシュを求める"""
        return (self.prefix[right] - self.power[right - left] * self.prefix[left]) % self.m

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


# セグメント木
class SegmentTree:
    def __init__(self, n, func, ide_ele, arr=None):  # 要素数, 計算に使う関数, 単位元
        self.n = n
        self.func = func
        self.ide_ele = ide_ele
        self.num = 1
        while self.num < self.n:
            self.num *= 2
        self.tree = [self.ide_ele] * (2 * self.num)
        if arr is not None:
            for i in range(len(arr)):
                self.tree[self.num + i] = arr[i]
            for i in range(self.num - 1, 0, -1):  # 上側
                self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):  # k番目をxに置き換える
        k += self.num
        self.tree[k] = x
        while 1 < k:  # 下の2つをfuncに入れた結果で親を更新していく(log)
            k >>= 1
            self.tree[k] = self.func(self.tree[2 * k], self.tree[2 * k + 1])

    def query(self, left, right):
        left += self.num
        right += self.num
        self.answer = self.ide_ele
        while left < right:
            if left % 2 == 1:
                self.answer = self.func(self.answer, self.tree[left])
                left += 1
            if right % 2 == 1:
                right -= 1
                self.answer = self.func(self.answer, self.tree[right])
            left >>= 1
            right >>= 1
        return self.answer

# Trie用ノードクラス
class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False
# トライ木
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

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
# Functions
#########################################################################

# l~rのうち，nで割り切れるものの個数
def get_division(left, right, n):
    return (right // n) - (left // n) + (1 if left % n == 0 else 0)


# 素数列挙
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


# 累積和 総和 = (r+1番目) - (l番目)
def pre_sum(l):
    a = [0 for _ in range(len(l) + 1)]
    for i in range(len(l)):
        a[i + 1] = a[i] + l[i]
    return a

# 累積xor和
def cum_xor(l):
    a = [0 for _ in range(len(l) + 1)]
    for i in range(len(l)):
        a[i + 1] = a[i] & l[i]
    return a

# 辞書ならこっちのほうが早い
from collections import Counter
def dictionary_of(lst):
    return Counter(lst)

# ダイクストラ法でstartからの全てのノードへの最短距離を求める
# edges[start] = [[nxt, cost], [nxt, cost], ...]
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

# オイラーツアーで部分木の要素数を列挙
def EulerTour(n, X, i0):
    done = [0] * n
    Q = [~i0, i0] # 根をスタックに追加
    ET = []
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            ET.append(i)
            for a in X[i][::-1]:
                if done[a]: continue
                Q.append(~a) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加
        
        else: # 帰りがけの処理
            ET.append(~i)
    
    return ET

# ワーシャルフロイドでO(N**3)で最短経路
# costs[i] = [cost_i0, cost_i1,...] の2重リスト
def floyd(costs: list):
    N = len(costs)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if costs[i][k] + costs[k][j] < costs[i][j]:
                    costs[i][j] = costs[i][k] + costs[k][j]
    return costs

# ユークリッド距離
def get_dist(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# 最大公約数
def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 最小公倍数
def get_lcm(a, b):
    return a // get_gcd(a, b) * b

# 素数列挙 O(N**0.5), 空間N
def get_primes(left, right):
    if left > right or right < 2:
        return []
    left = max(2, left)
    limit = int(math.isqrt(right))
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
    n = right - left + 1
    is_prime_range = [True] * n
    for prm in seed_primes:
        start = max(prm * prm, (left + prm - 1) // prm * prm)
        start_idx = start - left
        if start_idx < n:
            length = (n - 1 - start_idx) // prm + 1
            is_prime_range[start_idx:n:prm] = [False] * length
    return [left + i for i, is_p in enumerate(is_prime_range) if is_p]

# LCS部分文字列一致？
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

def lis(seq):
    LIS = [seq[0]]
    for i in range(len(seq)):
        if seq[i] > LIS[-1]:
            LIS.append(seq[i])
        else:
            LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]
    return LIS, len(LIS)

# 辞書作るだけ
# {名前: その数}
def make_dictionary(lst):
    d = {}
    for n in lst:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    return d

# 繰り返し二乗法
def modpow(a, n):
    ans = 1
    tmp = a
    while 1 <= n:
        if n % 2 == 1:
            ans *= tmp
        tmp *= tmp
        n = n >> 1
    return ans


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


def RLE_for(sequence):

    #戻り値の初期化
    comp_seq = list() # 圧縮されたデータのリスト
    lengths = list() # データの連続する長さのリスト

    # 最初の要素を記録
    comp_seq.append(sequence[0])
    temp = sequence[0]
    length = 1

    # 2番目から最後まで
    for i in range(1, len(sequence)):
        if sequence[i] != temp:  # 新しいデータが来たら、これまでのデータとその長さを記録
            lengths.append(length)
            comp_seq.append(sequence[i])
            temp = sequence[i]
            length = 1
        else: # 前と同じデータが来たら、lengthをインクリメント
            length += 1

    # 最後にlengthを追加
    lengths.append(length)

    return comp_seq, lengths

# 時計回りに回転
def rotate(grid):
    H, W = len(grid), len(grid[0])
    tmp = [["" for _ in range(W)] for __ in range(H)]
    for i in range(H):
        for j in range(W):
            tmp[i][j] = grid[H - 1 - j][i]
    return tmp

# BFS
# visited = [[False for _ in range(W)] for _ in range(H)]
# visited[starti][startj] = True
# while q:
#     i, j = q.popleft()
#     if visited[i][j]:
#         continue
#     visited[i][j] = True
#     for di, dj in drct:
#         ni, nj = i+di, j+dj
#         if 0 <= ni <= H-1 and 0 <= nj <= W-1 and grid[ni][nj] == ".":
#             if visited[ni][nj]:
#                 print(f"Yes")
#                 return
#             if not visited[ni][nj]:
#                 q.append((ni, nj))


"""
トポロジカルソートを行い、
・順序が存在するか
・それが一意か
を判定する
Returns:
    (is_dag, is_unique, order)
"""
def topo_sort_unique(N, graph):
    indeg = [0] * N
    for v in range(N):
        for nxt in graph[v]:
            indeg[nxt] += 1
    q = deque()
    for i in range(N):
        if indeg[i] == 0:
            q.append(i)
    order = []
    is_unique = True
    while q:
        if len(q) > 1:
            is_unique = False
        v = q.popleft()
        order.append(v)
        for nxt in graph[v]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    if len(order) != N:
        return False, False, []
    return True, is_unique, order

# Z-Algorithm
# 文字列の部分列
def z_algo(S):
    N = len(S)
    A = [0] * N
    i = 1
    j = 0
    A[0] = length = len(S)
    while i < length:
        while i + j < length and S[j] == S[i + j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while length - i > k < j - A[k]:
            A[i + k] = A[k]
            k += 1
        i += k
        j -= k
    return A

#########################################################################

if __name__ == "__main__":
    main()