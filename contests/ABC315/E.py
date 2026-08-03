"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < wanna solve green
"""
###################################################

import sys
sys.setrecursionlimit(10 ** 7)
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
    1をルートにもつ木全てを列挙する。読まなければならない順は
    DFSでできる
    親から子に降りるだけにすれば余計なものは排除できる
    再帰できれいに解けそう
    """

    N = int(input())

    graph = [[] for _ in range(N)] # iを読むために必要なノード
    for parent in range(N):
        l = i_list()
        for i in range(1, l[0]+1):
            child = l[i] - 1
            graph[parent].append(child)
    
    st = set() # すでに読んだ
    def solve(now, graph):
        if now in st:
            return
        if len(graph[now]) == 0:
            if now not in st and now != 0:
                print(now+1, end=" ")
                st.add(now)
        else:
            for child in graph[now]:
                if child not in st:
                    solve(child, graph)
            if now != 0:
                print(now+1, end=" ")
            st.add(now)
    
    solve(0, graph)
        
    # print(graph)


    return
######################################################

if __name__ == "__main__":
    main()
