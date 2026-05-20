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

def RLE_for(sequence):

    #戻り値の初期化
    comp_seq = list() # 圧縮されたデータのリスト
    lengths = list() # データの連続する長さのリスト

    # 最初の要素を記録
    comp_seq.append(sequence[0])
    temp = sequence[0]
    length = 1

    # 2番目から最後まで
    for i in range(1, len(sequence)):
        if sequence[i] != temp:  # 新しいデータが来たら、これまでのデータとその長さを記録
            lengths.append(length)
            comp_seq.append(sequence[i])
            temp = sequence[i]
            length = 1
        else: # 前と同じデータが来たら、lengthをインクリメント
            length += 1

    # 最後にlengthを追加
    lengths.append(length)

    return comp_seq, lengths

def main():

    N = int(input())
    P = i_list()
    
    """
    差の正負で圧縮して数える
    """

    l = []
    for i in range(N-1):
        if P[i] < P[i+1]:
            l.append(1)
        else:
            l.append(-1)
    
    L, n_list = RLE_for(l)
    # print(L, n_list)

    if len(L) < 3 :
        print(0)
        return
    count = 0
    for i in range(len(L) - 2):
        if (L[i], L[i+1], L[i+2]) == (1, -1, 1):
            count += n_list[i] * n_list[i+2]
    print(count)
            

    return
######################################################

if __name__ == "__main__":
    main()
