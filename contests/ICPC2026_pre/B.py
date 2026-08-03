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


def main():

    while 1:
        N = int(input())
        if N == 0:
            return
        S = list(input())
        st = set()
        for c in S:
            st.add(c)
        if len(st) <= 1:
            print("IMPOSSIBLE")
            continue
        else:
            for i in range(N-1):
                if S[i] != S[i+1]:
                    S[i], S[i+1] = S[i+1], S[i]
                    break
        print("".join(S))

######################################################

if __name__ == "__main__":
    main()