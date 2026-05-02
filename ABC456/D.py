"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < tired
"""
###################################################

# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
MOD = 998244353
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
    (文字aで終わるもの) = (他の文字で終わるもの - (今までの)文字aで終わるもの) + ((今までの)文字aで終わるもの) + 1
                       = (他の文字で終わるもの) + 1
    """

    S = list(input().strip())
    d = defaultdict(int)

    total = 0
    for c in S:
        new = (total + 1) % MOD # (他の文字で終わるもの) + 1
        total = (total + new - d[c]) % MOD # 今まであった + 新しくできた - そのまま引き継いだ
        d[c] = new

    print(total)

    return
######################################################

if __name__ == "__main__":
    main()
