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

        onumbers = [i for i in range(1, n + 1) if S[i] == 'o']

        mxm = min(7, len(onumbers))
        found = False

        for m in range(1, mxm + 1):
            for cmb in itertools.combinations_with_replacement(onumbers, m):
                if sum(cmb) != n:
                    continue
                dp = [False for _ in range(n + 1)]
                dp[0] = True
                
                is_valid = True
                
                for val in cmb:
                    for j in range(val, n)[::-1]:
                        if dp[j - val]:
                            if S[j] == 'x':
                                is_valid = False
                                break
                            dp[j] = True
                            
                    if not is_valid:
                        break
                        
                if not is_valid:
                    continue
                if all(dp[i] for i in onumbers):
                    ans.append(m)
                    found = True
                    break
                    
            if found:
                break
        if not found:
            ans.append(7)
    for a in ans:
        print(a)

    return
######################################################

if __name__ == "__main__":
    main()
