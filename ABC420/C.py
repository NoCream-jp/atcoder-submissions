"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗   <  !!!
                    ████╝

"""

###################################################
# 入力
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
# import bisect

# from itertools import permutations as p

##################################################


def main():
    N, Q = i_map()
    A, B = i_list(), i_list()
    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])

    for i in range(Q):
        q = list(input().split())
        c = q[0]
        X, V = int(q[1]), int(q[2])
        X -= 1
        if c == "A":
            a, b = A[X], B[X]
            mn = min(a, b)
            A[X] = V
            if V < b:
                ans += V - mn
            else:
                ans += b - mn
            print(ans)
        else:
            a, b = A[X], B[X]
            mn = min(a, b)
            B[X] = V
            if V < a:
                ans += V - mn
            else:
                ans += a - mn
            print(ans)
        # print("A", A)
        # print("B", B)


######################################################

if __name__ == "__main__":
    main()
