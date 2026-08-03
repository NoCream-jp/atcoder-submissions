"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < 42222222

"""

###################################################
# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
# MOD = 998244353
drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def c_list():
    return list(input().split())


# from collections import defaultdict
# from sortedcontainers import SortedList
# from collections import deque
# import heapq
# import math
# import bisect

# from itertools import permutations as p

##################################################


def main():
    N, K = i_map()

    num = K // (2**N)  # まずnumを2**N個並べて，Kになるようにgapを足していく
    ans = [num for _ in range(2**N)]

    gap = K - num * (2**N)  # 2**Nとの差(< 2**N)
    # print("gap", gap)

    # 10なら
    # i = 0, 5, 2, 7, ..が正解
    # 真ん中を埋めていかないと偏ってダメ
    # 10100000 00001010が2と0の差とられてだめになるから
    # 10001000 10001000 で埋めていきたい

    if gap > 0:
        ans[0] += 1
        gap -= 1

    if gap > 0:
        step = (2**N) // gap
        for i in range(1, gap + 1):
            ans[i * step] += 1

    print(int(bool(gap)))  # Uは絶対1か0
    # print("len(ans)", len(ans))
    print(*ans)


######################################################

if __name__ == "__main__":
    main()
