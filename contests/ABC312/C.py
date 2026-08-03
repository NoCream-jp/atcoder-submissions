"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < wanna solve green
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

# OKな売り手AがOKな買い手Bより多ければtrue
def check(X, A, B):
    acount, bcount = 0, 0
    for i in range(len(A)):
        if A[i] <= X:
            acount += 1
    for i in range(len(B)):
        if X <= B[i]:
            bcount += 1
    return bcount <= acount

def main():

    """
    値段で二分探索
    X円で売ってもよい人がX円で買ってもよいと考える
    人以上であるとき、もっと安くできる。
    X円で売ってもいい人がX円で買ってもいいと考える
    人未満であるとき、もっと高くしないといけない。

    チェックはO(N)だがソートしなければならないので
    O(NlogN)で解ける
    """
    N, M = i_map()
    A = i_list()
    B = i_list()
    A.sort()
    B.sort()

    l, r = 0, 10**9 + 1
    while l <= r:
        mid = (l+r)//2
        if check(mid, A, B):
            r = mid - 1
        else:
            l = mid + 1
    print(l)


    return
######################################################

if __name__ == "__main__":
    main()
