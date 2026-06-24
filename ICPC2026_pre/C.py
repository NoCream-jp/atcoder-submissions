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

##################################################
from collections import deque

def main():

    while 1:
        N, K = i_map()
        if N == 0 and K == 0:
            return
        S = input()
        q = deque()
        mx = 0
        count = 0
        for c in S:
            if c == "_":
                q.append(c)
                if count < K:
                    count += 1
                else:
                    while q:
                        popped = q.popleft()
                        # print(F"{popped} popped")
                        if popped == "_":
                            break
            elif c == "o":
                q.append(c)
            else:
                count = 0
                q = deque()
            mx = max(mx, len(q))
        # print(q, mx)
        print(mx)




    return
######################################################

if __name__ == "__main__":
    main()