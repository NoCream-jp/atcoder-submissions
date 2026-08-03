"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < tired
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
# 最大公約数
def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 最小公倍数
def get_lcm(a, b):
    return a // get_gcd(a, b) * b

# 素数列挙
# 素数列挙 O(N**0.5), 空間N
def get_primes(left, right):
    if left > right or right < 2:
        return []
    left = max(2, left)
    limit = int(math.isqrt(right))
    seed_primes = []
    if limit >= 2:
        is_prime_small = [True] * (limit + 1)
        is_prime_small[0] = is_prime_small[1] = False
        for i in range(2, int(math.isqrt(limit)) + 1):
            if is_prime_small[i]:
                is_prime_small[i * i : limit + 1 : i] = [False] * len(
                    is_prime_small[i * i : limit + 1 : i]
                )
        seed_primes = [p for p, is_p in enumerate(is_prime_small) if is_p]
    n = right - left + 1
    is_prime_range = [True] * n
    for prm in seed_primes:
        start = max(prm * prm, (left + prm - 1) // prm * prm)
        start_idx = start - left
        if start_idx < n:
            length = (n - 1 - start_idx) // prm + 1
            is_prime_range[start_idx:n:prm] = [False] * length
    return [left + i for i, is_p in enumerate(is_prime_range) if is_p]

def main():

    N, M = i_map()
    P = i_list()
    ans = 1
    for n in P:
        ans = get_lcm(ans, n)
        if M < ans:
            print("No")
            return
            
    print("Yes")

    return
######################################################

if __name__ == "__main__":
    main()
