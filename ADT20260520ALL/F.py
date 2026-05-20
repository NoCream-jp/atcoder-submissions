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

##################################################
def check(Q, A, B, acount):
    N = len(Q)
    bcount = float('inf')
    for i in range(N):
        Q[i] -= A[i] * acount
        if Q[i] < 0:
            return -1
        bcount = min(bcount, Q[i] // B[i])
    return bcount

def main():

    """
    Aをマックスまで作って、そこからBに切り替えるだけの全探索
    """

    N = int(input())
    Q = i_list()
    A = i_list()
    B = i_list()

    ans = 0
    for acount in range(1, max(Q) + 2):
        c = check(Q, A, B, acount)
        if c == -1:
            break
        print(acount, c)
        ans = max(ans, acount + c)

    print(ans)

    return
######################################################

if __name__ == "__main__":
    main()
