"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < abc465?
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
from collections import Counter
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations

##################################################


def main():

    """
    それぞれの個数数えるだけで行けそう、Nがint型じゃないほうがよさそうなことに注意？
    包除みたいにO(1)で最後につじつま合わせ
    6個求めないといけない
    a, b, c, ab, bc, ca

    a:3の倍数の数は、割るだけ
    b:十進表記に3が含まれる数は、一つも含まない数が9進数になるから簡単
    c:ちょうど3種類の数字は、これも0で場合分けして0以外の9C3と4進数

    ab: 3の倍数 かつ 十進表記に3が含まれる数は、3を使ったか使ってないかで
        桁の数の合計が3の倍数かどうか
    bc: 

    ca: 

    無理そう

    桁ごとに見れないか
    桁そこまでにある大丈夫な数の集合？
    メタ読み：http://qiita.com/pinokions009/items/1e98252718eeeeb5c9ab
    """
    


    return
######################################################

if __name__ == "__main__":
    main()