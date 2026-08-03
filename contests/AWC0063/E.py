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
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations as p

##################################################
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

def main():

    N, Q = i_map()
    C = i_list()
    st = SegmentTree(N, sum, 1)
    for t in range(Q):
        query = i_list()
        # if query[0] == 1:
            

######################################################

if __name__ == "__main__":
    main()
