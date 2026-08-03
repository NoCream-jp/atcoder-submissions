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


def main():
    N = int(input())
    S = input()
    if S[-3:] == "tea":
        print("Yes")
    else:
        print("No")


######################################################

if __name__ == "__main__":
    main()
