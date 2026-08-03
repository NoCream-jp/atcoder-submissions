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
        n, m = i_map()
        if n == m == 0:
            return
        lst = [int(input(), 2) for _ in range(n)]

        if m < n:
        # if 1:
            # print("m小さくてdpで解きたいとき")
            dp = [[-1 for _ in range(2**m)] for _ in range(n)]
            dp[0][0] = 0
            num = lst[0]
            dp[0][num] = 1
            for i in range(1, n):
                num = lst[i]
                for j in range(2**m):
                    # print("j^m", j^num)
                    if dp[i-1][num^j] != -1:
                        dp[i][j] = max(dp[i-1][j], dp[i-1][j^num] + 1)
                    else:
                        dp[i][j] = dp[i-1][j]
            # for d in dp:
            #     print(d)
            print(dp[-1][0] if dp[-1][0] != -1 else 0)
        else:
            # print("n大きくてbit全探索で解きたいとき")
            ans = 0
            for i in range(2**n):
                temp, count = 0, 0
                for j in range(n):
                    if (i >> j) & 1:
                        temp ^= lst[j]
                        count += 1
                if temp == 0:
                    ans = max(ans, count)
            print(ans)
                            
    return
######################################################

if __name__ == "__main__":
    main()