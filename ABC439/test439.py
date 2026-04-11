"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ wheres my green

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

# from sortedcontainers import SortedList
# from collections import deque
import heapq

# import math
import bisect

from itertools import permutations as p

##################################################


def main():
    N = int(input())
    S = input()

    """
    ある手について考えた時、負けていると考えなくてよい
    勝っていれば、それまでの最善手にプラス1
    あいこならそのまま引き継ぐ
    dp[手][i回目] = max(dp[それ以外の手][i-1回目], dp[手][i回目])で
    最大の数字を書き込んでいける
    """

    hand = ["R", "S", "P"]
    dp = {t: [0 for _ in range(N + 1)] for t in hand}  # dp[手][回目]

    def judge(takahashi, aoki):
        if (
            (takahashi == "R" and aoki == "P")
            or (takahashi == "S" and aoki == "R")
            or (takahashi == "P" and aoki == "S")
        ):
            return 0
        elif takahashi == aoki:
            return 1
        return 2

    for i in range(N):
        aoki = S[i]
        for takahashi in hand:
            result = judge(takahashi, aoki)
            if result == 0:  # 負ける手は出せない
                dp[takahashi][i] = -1
            elif result == 1:  # あいこだった場合、一つ前の異なる手をそのまま
                for h in hand:
                    if h != takahashi:
                        dp[takahashi][i] = max(dp[h][i - 1], dp[takahashi][i])
            else:
                for h in hand:
                    if h != takahashi:
                        dp[takahashi][i] = max(dp[h][i - 1] + 1, dp[takahashi][i])

    ans = max([dp[h][-2] for h in hand])  # 右端に0追加してるので右から二番目
    print(ans)
    return


######################################################

if __name__ == "__main__":
    main()
