"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < am i worth ARC?
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
    Q'を作る際必ず1を一番左に持ってくる
    96741 8325
    ↓
    14769 8325
    1が最初から左にあれば2を、12が最初から左にあれば3をその次に持ってくることで構築できる
    1がどこにあるかだけ考えてもN通りあるからどうするか
    逆算なのがすごく苦手
    1が-1番目にあれば、
    Q  9.......1
    Q' 1.......9
    P  1(7!)9 -> 8!
    """

    return
######################################################

if __name__ == "__main__":
    main()
