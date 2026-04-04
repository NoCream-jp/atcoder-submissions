"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ <wktk
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
# from tkinter import W
from atcoder.dsu import DSU

# Fenwick Tree (Binary Indexed Tree)
from atcoder.fenwicktree import FenwickTree

# Segment Tree
from atcoder.segtree import SegTree

# Lazy Segment Tree
from atcoder.lazysegtree import LazySegTree

# Math (pow_mod, inv_mod, crt, floor_sumなど)
# from atcoder.math import *

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
# from atcoder.string import *

from collections import defaultdict
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect

from itertools import permutations as p

##################################################


def main():
    
    H, W = i_map()
    grid = [["." for _ in range(W)] for __ in range(H)]

    for i in range(H):
        for j in range(W):
            if i == 0 or j == 0 or i == H - 1 or j == W - 1:
                grid[i][j] = "#"
    
    for r in grid:
        print("".join(r))
#########################################################################

if __name__ == "__main__":
    main()
