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

    # 前計算 (j = 1 のときを基準にする)
    left[A[0]] += 1
    for i in range(2, N):
        right[A[i]] += 1
        
    result = 0
    # 最初は left に A[0] しかないので、この計算だけ
    for k in left:
        result += left[k] * right[k]
    # j = 1
    ans = result - left[A[1]] * right[A[1]]
    
    # ans 更新 (j を 2 から N-2 まで動かす)
    for j in range(2, N - 1):
        num = A[j-1]
        result -= left[num] * right[num]  # 古い値を引く
        left[num] += 1                           # leftを更新
        result += left[num] * right[num]  # 新しい値を足す
        
        rnum = A[j]
        result -= left[rnum] * right[rnum]
        right[rnum] -= 1
        result += left[rnum] * right[rnum]
        
        ans += result - left[A[j]] * right[A[j]]
        
    print(ans)

    return
######################################################

if __name__ == "__main__":
    main()
