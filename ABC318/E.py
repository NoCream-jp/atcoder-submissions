"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < weee
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


def main():

    """
    見ているjの左右にある、
    同じ数字の組の数を更新していく。
    jが1動いただけではせいぜい左右それぞれ1種類しか変わらない
    ので、差分だけ再計算できる。

    はじめ2~N-1について全部の組の個数を持っておく
    j=1の場合の答えを計算する
    jを1からN-2まで動かして、通り過ぎた数(のみ)について
    「右から取り除き左に追加して掛け算をもう一度行う」をする

    そのあと答えに加算する
    """

    N = int(input())
    A = i_list()
    left = defaultdict(int)
    right = defaultdict(int)
    result = defaultdict(int)

    # 前計算
    left[A[0]] += 1
    for i in range(2, N):
        right[A[i]] += 1
        result[A[i]] += A[2:].count(A[i])
    print(left, right, result)
    
    # j=1のときだけ
    ans = 0
    j = 1
    ans += left[A[0]] * right[A[0]] - left[A[j]] * right[A[j]]
    print(f"1回目のans: {ans}")

    # ans 更新
    for j in range(2, N-1):
        left[A[j-1]] += 1
        right[A[j]] -= 1
        result[A]
        print(left, right)
        ans += left[A[j]] * right[A[j]] - left[A[j-1]] * right[A[j-1]]
        print(f"{j}回目のans: {ans}")




    return
######################################################

if __name__ == "__main__":
    main()
