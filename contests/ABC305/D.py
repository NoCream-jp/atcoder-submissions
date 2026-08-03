"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < try to solve light blue prob
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
# 累積和 総和 = (r+1番目) - (l番目)
def cum_sum(l):
    a = [0 for _ in range(len(l) + 1)]
    for i in range(1, len(l)+1):
        if i%2 == 1:
            a[i] = a[i-1]
        else:
            a[i] = a[i-1] + (l[i] - l[i-1])
    return a

def main():

    """
    端の処理が面倒なだけの二分探索
    累積和を取っておいて二分探索で得たインデックスを使って計算する
    要素と同じ場合はスルー
    異なる場合のみ、睡眠中か覚醒中かを判定しないといけない

    """

    N = int(input())
    A = i_list()
    cA = cum_sum(A)
    # print(cA)
    Q = int(input())
    for _ in range(Q):
        l, r = i_map()
        ans = 0
        lidx = bisect.bisect_right(A, l)
        ridx = bisect.bisect_right(A, r)
        # lidxは同じか小さい
        # ridxは同じか大きい
        # 累積和を取れる形にするにはlより大きく、rより小さいものに合わせなければならないが
        # 同じ睡眠中にlrがあった場合はそうするとr < lとなってしまう
        # 誤差を持っておいてちぢめることを考えていたが「右に合わせる」ようにすればよさそう
        # 累積和は睡眠中も含めることで場合分け減らせそう
        # print(f"lidx{lidx}, ridx={ridx}")
        # l
        # 奇数なら覚醒の終わりまたは途中　誤差は持たない
        # 偶数なら睡眠の終わりまたは途中なので　右に揃えて誤差を持つ
        if lidx % 2 == 0:
            # print(f"ansに{abs(A[lidx] - l)}を足す")
            ans += abs(A[lidx] - l)
        # r
        # 偶数なら左に揃えて誤差を負にする
        if ridx % 2 == 0:
            # print(f"ansから{abs(A[ridx] - r)}を引く")
            ans -= abs(A[ridx] - r)
        # print(f"ans={ans}, lidx={lidx}, r={ridx}")
        ans += cA[ridx] - cA[lidx]
        # print(f"ans={ans}\n")
        print(ans)



    return
######################################################

if __name__ == "__main__":
    main()
