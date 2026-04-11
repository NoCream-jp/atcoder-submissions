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


from collections import defaultdict

# from sortedcontainers import SortedList
# from collections import deque
# import heapq
# import math
import bisect

# from itertools import permutations as p

##################################################


def main():
    N, K = i_map()

    """
    木を上から作って間に合う
    """
    flag = 0  # Xが1になるか0になるか
    tmp = 1
    while N != 0:
        ans = []
        N -= 1
        if K % 2 == 0:
            for i in range(2**tmp):
                ans.append(K // 2)
        else:
            for i in range(2**tmp // 2):
                ans.append(K // 2 + 1)
                ans.append(K // 2)
                flag = 1
        K //= 2
        tmp += 1
        print(ans, flag)


######################################################

if __name__ == "__main__":
    main()
