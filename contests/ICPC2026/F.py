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
        s, k = i_map()
        if s == k == 0:
            break
        if k == 1:
            print(s)
            continue
        if s == 1:
            k += 1
            s = k + 1
        if (s * s + 1 >= k):
            if (s * s + 1 == k):
                print(s)
                continue
            ans = 0
            right = 0
            left = 1
            for i in range(s -1, -1, -1):
                right = left + 2 * i + 1
                num = s - i
                # print(f"! {num=} {left=} {right=}")
                if right == k:
                    ans = s
                    break
                if right > k:
                    index = k - left
                    if index % 2 == 0:
                        ans = num
                    else:
                        ans = num + index // 2
                    break
                left = right
            print(ans)
            continue
        else:
            i = 0
            right = 0
            left = s * s + 1
            index = k - left
            num = index // (s* 2)
            index = index%s
            if index % 2 == 1:
                ans = num + 1 + s
            else:
                ans = index // 2        
            
            
            print(ans)



    return
######################################################

if __name__ == "__main__":
    main()