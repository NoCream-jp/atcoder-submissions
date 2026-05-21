"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < wanna solve green
"""
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
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations as p

from atcoder.lazysegtree import LazySegTree

##################################################


# ----
from atcoder.lazysegtree import LazySegTree

def op(x, y):
    return (x[0] + y[0], x[1] + y[1])

def mapping(f, x):
    return (x[0] + f * x[1], x[1])

def composition(f, g):
    return f + g

# 【修正1】関数ではなく、値を直接定義する
e = (0, 0)
id_ = 0

# ----


def main():

    """
    % で範囲指定するimosみたいに、端だけメモする。
    何周するかの情報も持たせる必要がある
    例えば
    5 1
47 0 0 0 0
0
    ↓
    9 10 10 10 9

    ならどこからどこまでが9で
    どこからどこまでが10なのかは計算で分かる。
    毎回今いる部分だけ計算することができるか

    つまりやりたいことは
    ・区間への高速な一括加算
    ・ある要素の高速な取得（これは長さ1の区間取得で再現できる）
    ↓
    lazy_segtree
    """

    

    N, M = i_map()
    A = i_list()
    B = i_list()

    seg = LazySegTree(op, e, mapping, composition, id_, N)

    # seg.apply(2, 5) # インデックス2に5を加算
    # seg.apply(2, 5, 5) # [2, 4)に加算
    # print(seg.prod(0, 2)) # インデックス0~1の和の取得
    
    for i in range(M):
        ball = B[i]
        # 一周しないぶんの追加の値、一周するぶんの値
        # Nより大きくなってしまうかどうかで場合分け、ball <= Nならbigは無い
        big, small = ball // N + 1, ball // N
        big_l = (B[i] + 1) % N
        big_r = ((big_l + big) % N)
        small_l = (big_r + 1) % N
        small_r = ((small_l + small) % N)
        print(f"big={big}, small={small}")
        print(f"big_l={big_l}, big_r={big_r}")
        print(f"small_l={small_l}, small_r={small_r}")

    return
######################################################

if __name__ == "__main__":
    main()
