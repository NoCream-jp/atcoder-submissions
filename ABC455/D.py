"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < my cat running
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
    足元をメモしなおしていく，
    最後にiについて上から見ていくことを繰り返す走査をするが
    すでに通ったものは飛ばす

    足元からのほうがいい．だから自分の上をメモする．取られたやつも忘れずに
    取られたやつように配列がいる
    """

    N, Q = i_map()

    l = [-1 for _ in range(N+1)] # 自分の上
    l2 = [-1 for i in range(N)] # 自分の下
    for _ in range(Q):
        c, p = i_map() # 4を5にのせる
        c -= 1
        p -= 1
        # 4の下の上を-1に
        # l2[c]が-1なら，端にスペース作って書き換えさせる
        l[l2[c]] = -1
        # 4の下を5に
        l2[c] = p
        # 5の上を4に
        l[p] = c

    # 下が-1のやつだけ見る．なぜなら一番下のやつらは絶対にインデックスが変わってないから
    for foot in range(N):
        if l2[foot] != -1:
            print(0, end=" ")
            continue
        count = 1

        # 見てるやつの上が-1ならおわり，そうでないなら追いかける
        while l[foot] != -1:
            foot = l[foot]
            count +=1
        print(count, end=" ")

    return
######################################################

if __name__ == "__main__":
    main()