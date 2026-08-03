"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < wanna solve green
"""
###################################################
# import sys
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
    a, b, cの倍数にするために必要な最小回数を
    すべての項に対して求めておく。
    -> その列挙にどれだけかかるかわからない
    
    被ったらどうするか
    被ったらヒープを使うことで解決できる？
    難しそう

    a,b,cの順に揃えたい値を決める
    たとえaの倍数がすでにあっても、それを書き換えるほうが良いケースはある
    
    ある数Xがa,b,cについてそれぞれの倍数であるかどうかの
    状態は8しかない。
    8Nの中でdp
    
    """

    # N, a, b, c = i_map()
    # A = i_list()


    
    return
######################################################

if __name__ == "__main__":
    main()
