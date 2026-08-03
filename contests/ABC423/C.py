"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < chill

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


# from collections import defaultdict
# from sortedcontainers import SortedList
# from collections import deque
# import heapq
# import math
# import bisect
# from itertools import permutations as p

##################################################


def main():
    N, R = i_map()
    R -= 1
    lst = i_list()

    """
    引き返す地点を探す．
    端から1が続くようならそこへは行かなくてよい.
    """

    if sum(lst) == N:
        print(0)
        return

    left, right = 0, N - 1
    while lst[left] == 1 and left < R:
        left += 1
    while lst[right] == 1 and R < right:
        right -= 1

    L = lst[:]
    leftcost = 0  # Rから左まで行くためのコスト
    for i in range(left, R + 1)[::-1]:
        if L[i] == 1:
            L[i] = 0
            leftcost += 1
    close = 0  # 端から端まで全部閉じるためのコスト(端まで行ったドアの状態前提で)
    for i in range(left, right + 1):
        if L[i] == 0:
            close += 1
        else:
            close += 2
    ans1 = leftcost + close

    ##################################右
    L = lst[:]
    rightcost = 0  # Rから右まで行くためのコスト
    for i in range(R, right + 1):
        if L[i] == 1:
            L[i] = 0
            rightcost += 1
    close = 0  # 端から端まで全部閉じるためのコスト(端まで行ったドアの状態前提で)
    for i in range(left, right + 1):
        if L[i] == 0:
            close += 1
        else:
            close += 2
    ans2 = rightcost + close

    print(min(ans1, ans2))


######################################################

if __name__ == "__main__":
    main()
