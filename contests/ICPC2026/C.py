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

    aa = []

    while 1:
        n = int(input())
        if n == 0:
            break
        l = i_list()
        
        left, right = 0, n-1
        for i in range(n-1):
            if l[i] > l[i+1]:
                left += 1
            else:
                break
        for i in range(1, n)[::-1]:
            if l[i-1] < l[i]:
                right -= 1
            else:
                break

        # print(f"{left =} {right =}")
        if left >= right:
            # print("!", 0)
            print(0)
            continue

        wall = l[left]
        temp = 0
        num = 0
        ans = 0
        for i in range(left+1, right+1):
            if i == right and wall < l[i]:
                temp = 0
                idx = right - 1
                while l[idx] > l[right] and idx > left:
                    temp += l[idx] - l[right]
                    idx -= 1
                ans += temp
                break

            if wall < l[i]:
                temp += l[i] - wall
                num += 1
            else:
                ans += temp
                temp = 0
                num = 0
                wall = l[i]
        # print("!",ans)
        print(ans)
    

######################################################

if __name__ == "__main__":
    main()