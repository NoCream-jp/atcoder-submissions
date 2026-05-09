"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < feel sick
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
    差分の差分を見たらどこに足せばいいかわかりそうな気はする
    見たことないDPだったら解けないのでそうじゃないとする

    答えのにぶたん
    答えは達成可能な最小値
    判定はすべてについてその値を超えられるギリまで「操作」できるか
    """

    N, K = i_map()
    A = i_list()
    # B = enumerate(A)
    B = []
    for i in range(N):
        B.append((A[i], i+1))

    l = 0
    r = max(A) + K * N + 100
    while l <= r:
        mid = (l + r) // 2
        count = 0 # 必要な操作の回数
        for i in range(N):
            num, ope = B[i]
            if num < mid:
                count += (mid - num + ope - 1) // ope
                # print(f"{num, ope}を{mid}にするため{(mid - num + ope - 1) // ope}回操作が必要")
            if K < count:
                break
        if K < count: # 大きすぎれば不可能なのでmidを左に
            r = mid - 1
        else: # 小さすぎればまだまだ可能なのでmidを右に
            l = mid + 1
    print(int(l-1))

    return
######################################################

if __name__ == "__main__":
    main()
