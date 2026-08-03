"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < difficult?
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

def upidx(l, medidx):
    medidx += 1
    while medidx < len(l)-1 and l[medidx] == False:
        medidx += 1
    return medidx
def downidx(l, medidx):
    medidx -= 1
    while 0 < medidx and l[medidx] == False:
        medidx -= 1
    return medidx
        

def main():

    """
    逆から読んで、最初にソートして削っていく（×印をつけていく）
    真ん中よりでかいのがなくなれば中央値を小さいほうにずらせばいい（ずらすのに全部でNかからない）
    ×ついたものは飛ばしてずらしていく

    常に奇数なのはうれしい
    ×つけるときはにぶたん
    """

    X = int(input())
    Q = int(input())
    l = [[X, True]] # (num, 使えるか)
    query = []
    for _ in range(Q):
        a, b = i_map()    
        l.append([a, True])
        l.append([b, True])
        query.append((a, b))

    l.sort()
    l_value = [l[i][0] for i in range(len(l))]
    medidx = len(l) // 2
    ans = []
    for a, b in query[::-1]:
        print(a, b)
        med = l[medidx][0]
        ans.append(med)
        if med < a and med < b:
            # medidxを減らす
            medidx = downidx(l, medidx)
        elif a < med and b < med:
            medidx = upidx(l, medidx)
        # xつける
        aidx = bisect.bisect_left(l_value, a)
        print(f"{a} {aidx}番目を見つけたので{aidx}にxをつける")
        l[aidx][1] = False
        bidx = bisect.bisect_left(l_value, b)
        print(f"{b} {bidx}番目を見つけたので{bidx}にxをつける")
        l[bidx][1] = False
        print("l", l)
        print(ans, medidx)
        print()




    return
######################################################

if __name__ == "__main__":
    main()
