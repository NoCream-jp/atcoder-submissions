###################################################
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
        n, d = i_map()
        if n == d == 0:
            return
        l = i_list()

        ans = 0

        while l:
            start = l[-1]
            # print(f"l: {l}")
            while l and start - d*2 <= l[-1]:
                # print(f"pop {l.pop()}, ans={ans}")
                l.pop()
            ans += 1

        
        print(ans)



######################################################

if __name__ == "__main__":
    main()