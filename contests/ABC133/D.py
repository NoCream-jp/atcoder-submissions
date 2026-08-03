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

def check(l, start):
    N = len(l)
    now = start
    for i in range(N):
        print(f"{now}をA[{i}]とA[{i-1}]から引く")
        l[i] -= now
        l[i-1] -= now
        print("l", l)
        if l[i] < 0 : return -1
        now = l[i]
    return sum(l)
    

def main():

    N = int(input())
    A = i_list()

    l, r = 0, A[0] + 1
    while l < r:
        B = A.copy()
        mid = (l + r) // 2
        result = check(B, mid)
        if result < 0:
            r = mid - 1
        elif 0 < result:
            l = mid + 1
        else:
            print(f"予測一つ目の値{l}")
            break
    print(l)


    return
######################################################

if __name__ == "__main__":
    main()
