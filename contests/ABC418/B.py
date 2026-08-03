"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗   < ABC 418
                    ████╝

"""


# 入力


def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def c_list():
    return list(input().split())


######################################################


def solve(s):
    if 3 <= len(s) and s[0] == s[-1] == "t":
        x = s.count("t")
        return (x - 2) / (len(s) - 2)
    return 0


def main():
    S = input()

    ans = 0
    for i in range(len(S) - 1):
        for j in range(i + 1, len(S)):
            if S[i] == S[j] == "t":
                ans = max(ans, solve(S[i : j + 1]))

    print(ans)


######################################################

if __name__ == "__main__":
    main()
