"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ green tea

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

# from sortedcontainers import SortedList
# from collections import deque
import heapq

# import math
import bisect

from itertools import permutations as p

##################################################


def main():
    N = int(input())

    """
    xを固定してyを全探索でも間に合いそう
    """

    check = [False for i in range(N + 1)]  # チェック用ここから解答すればいい
    ng = set()  # かぶったやつ
    for x in range(1, int(N ** (1 / 2)) + 1):
        right = int((N - x**2) ** 0.5) + 1
        for y in range(x + 1, right):
            number = x**2 + y**2
            check[number] += 1

    answer = []
    for i in range(len(check)):
        if check[i] == 1:
            answer.append(i)
    print(len(answer))
    print(*answer)

    return


######################################################

if __name__ == "__main__":
    main()
