"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < give me money?
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
from itertools import permutations

##################################################


def main():

    """
    どのアルファベット(N+1)//2以下ならOK
    でかいのから埋めていけばいい
    出現頻度の多い順に左から一つ飛ばしで埋めたいが
    N//2もなかった場合埋めるべきマスが余る
    その状態でほかの頻度の高い数を扱うとバグりそう

    ヒープキューで数と種類をもって前から見て置いていく?

    ソートして置いて、前からスワップしていくのが早そう？
    固まったらできない

    前から一個とばしで触るインデックスを決めて、それに
    今あるaの数ぶん沿う
    端が面倒だけどできる
    """
    
    T = int(input())
    for _ in range(T):
        d = defaultdict(int)
        S = input()
        N = len(S)
        for c in S:
            d[c] += 1
        q = []
        heapq.heapify(q)
        for k in d:
            heapq.heappush(q, (-d[k], k))
        # print(q)


        idx = 0
        ans = [False for _ in range(N)]
        end = False
        while q:
            if end:
                break
            num, c = heapq.heappop(q)
            num *= -1
            if (N+1)//2 < num :
                print("No")
                end = True
            while num:
                ans[idx] = c
                idx = (idx + 2) % N
                if ans[idx] and idx <= N-2:
                    idx += 1
                num -= 1
        if not end:
            print("Yes")
            print("".join(ans))


    return
######################################################

if __name__ == "__main__":
    main()
