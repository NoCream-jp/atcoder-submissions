"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < give me higher rate point !!!!
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

# x以上話した状態でk個取れるかどうか
def check(lst, x, k, startl, startr, startidx):
    # lstはlの昇順でソート済み
    nowl, nowr = startl, startr
    idx = startidx
    count = 1
    templ, tempr = -1, -1
    while startidx < len(lst)-1:
        l, r = lst[idx+1]
        if l <= nowr + x:
            idx += 1
            


def main():

    """
    mid以上離した状態でK個並べられるかどうかの結果が単調に変化する
    判定については、l,rをlの昇順に見ていって
    """
    N, K = i_map()
    lst = [tuple(i_map()) for _ in range(N)]
    lst.sort()

    # 必ず採用する一番左の布を決めておく
    startl, startr = float('inf'), float('inf')

    idx = 0
    for l, r in sorted(lst, key=lambda x:x[1]):
        if r < startr:
            startl = l
            startr = r
            break
        idx += 1

    
    print("s", startl, startr)

    # 数値で二分探索
    # lが0で終われば答えは-1
    l, r = 0, 10**9
    while l < r:
        mid = (l + r) // 2
        if check(lst, mid, K, startl, startr, idx):
            l = mid + 1
        else:
            r = mid - 1
    
    if l:
        print(l)
    else:
        print(-1)


    return
######################################################

if __name__ == "__main__":
    main()
