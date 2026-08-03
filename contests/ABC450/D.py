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


def main():

    """
    K未満に必ずなる.
    ある時点でK以上なら最小にKを足せばそれより小さくなるから
    つまり最小にKを足すということを繰り返せばその中で最小の瞬間がある
    最小が小さすぎると時間がかかるので，一気に次に小さい項より大きくなるまで
    O(1)で足したい．
    """

    N, K = i_map()
    A = i_list()
    mx, mn = max(A), min(A)
    ans = mx - mn
    heapq.heapify(A)
    for _ in range(N-1):
        



    

    return
######################################################

if __name__ == "__main__":
    main()
