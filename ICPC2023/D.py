"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < icpc!
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

# from collections import defaultdict
# from sortedcontainers import SortedList
# from collections import deque
# import heapq
# import math
# import bisect
import itertools

##################################################

"""
7以下確定なので6まで調べて最小を求める．
6個のn以下の数字の組み合わせを全列挙して
"""

def main():

    ans = []

    while 1:
        n = int(input())
        if n == 0:
            break
        S = input()

        max_bit = n.bit_length()

        bit_index = [i for i in range(max_bit)] # つかうbit番目
        for m in range(1, max_bit+1): # m個使う
            cmb = itertools.combinations_with_replacement(bit_index, m)
            print(cmb)
            for c in cmb: # cには何ビット目を使うかが入っている
                print(c)
                # ナップザック

        print()




            

    return
######################################################

if __name__ == "__main__":
    main()
