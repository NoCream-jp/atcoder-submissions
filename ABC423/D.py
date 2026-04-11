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
import heapq
# import math
# import bisect
# from itertools import permutations as p

##################################################


def main():
    N, K = i_map()
    l = [i_list() for i in range(N)]
    l.sort()

    """
    前の奴が出る時刻を優先度キューに入れる
    """

    time = []
    heapq.heapify(time)

    now = 0  # 店の人数
    nowtime = 0
    for a, b, c in l:
        if now + c <= K:
            heapq.heappush(time, (-(a + b), c))  # （退店時間，人数）
            nowtime = a
        else:
            count = 0
            intime = -1
            while count < c:
                count += time[0][1]  # 客をじゅうぶん出すまで
                now -= time[0][1]
                intime = -time[0][0]  # 時間はpopされた中で一番遅かったもの
                heapq.heappop(time)
            nowtime = intime
            heapq.heappush(time, (-(intime + b), c))
        now += c
        print(nowtime)


######################################################

if __name__ == "__main__":
    main()
