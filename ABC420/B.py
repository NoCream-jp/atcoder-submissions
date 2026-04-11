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
    N, M = i_map()
    l = [input() for _ in range(N)]
    score = [0 for _ in range(N)]
    for j in range(M):
        l1 = []
        l0 = []
        count = 0  # 1を数える
        for i in range(N):
            if l[i][j] == "1":
                count += 1
                l1.append(i)
            else:
                l0.append(i)
        # print(l1, l0, count, l[i])
        if N // 2 < count:  # 1の方が多い
            for p in l1:
                score[p] += 1
        else:
            for p in l0:
                score[p] += 1
    # print(score)
    mn = min(score)
    ans = []
    for i in range(N):
        if score[i] == mn:
            ans.append(i + 1)
    print(*sorted(ans))


######################################################

if __name__ == "__main__":
    main()
