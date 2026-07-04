"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < abc465?
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
from collections import Counter
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations

##################################################


def main():

    """
    xを小さくするならkで商を取る
    大きくするならkで割ってxになるような数から選ぶ
    11 9 3 なら
    一回小さくするのは確定だけど
    ちょうどいいところまで大きくしてから割るのか
    割ってからなのかわからない

    割るのがa,
    かけてk-1まで足せるのがb
    bを何回かとaで〇〇大きいは達成できる。
    bは上限がk-1だから、例えばb2a1でx+1を作れるとか？

    yのほうを近づければ良い
    """

    T = int(input())
    for t in range(T):
        x, y, k = i_map()

        ans = 0
        while x != y:
            if y < x:
                x //= k
                ans += 1
            else:
                y //= k
                ans += 1
        print(ans)

    return
######################################################

if __name__ == "__main__":
    main()