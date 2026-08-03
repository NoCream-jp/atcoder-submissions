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
        N = int(input())
        if N == 0:
            return
        l = i_list()

        ans = -1
        for i in range(N):
            num = l[i]
            if num == 1 or num == 2:
                num += 13
            ans = max(ans, num)
        
        if 13 < ans:
            ans -= 13 
        print(ans)

######################################################

if __name__ == "__main__":
    main()