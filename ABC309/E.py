"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < difficult 
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
    ドミノ倒しみたいに最大値を更新しながら
    O(N)でマークアップすればいいので、
    あとは代ごとに並べる。
    i代目の人の集合の配列、人iが何代目かという配列
    を用意すべき
    """

    N, M = i_map()
    P = i_list()
    # 人iが何代目なのか
    rankOf = [0 for _ in range(N)]
    # i代目に誰がいるのか
    whoIn = [0 for _ in range(N)]

    
    
    return
######################################################

if __name__ == "__main__":
    main()
