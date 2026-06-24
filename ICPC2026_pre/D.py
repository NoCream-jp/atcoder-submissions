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

def shift(l, n):
    return l[n:] + l[:n]

def main():
    d = {"udfblr"[i]: i for i in range(6)}
    print(d)

    while 1:
        N = int(input())
        if N == 0:
            return
        # サイコロ全ての目
        # u1 d1 f1 b1 l1 r1
        dice = [
            i_list() for _ in range(N)
        ]
        print(dice)
        
        # サイコロ全てについて使うかどうかの状態を表す整数 i の列挙
        # サイコロ1以外の全てについて、天地どちらかを表す整数 j の列挙
        # 各サイコロについて、どの面を天地にするかを表す整数 k の列挙
        # 各サイコロについて、どの面をシフトで正面に持ってくるか l
        use = []
        for i in range(2 ** (N)): # 使う1
            for j in range(2 ** (N-1)): # 天なら1
                for k in range(3**N): # どの面を天地にするか
                    for l in range(4**N): # l回シフトしたものを使う
                        use.append((i, j, k, l))
        
        result = 0
        for i, j, k, l in use:
            # i番目のサイコロすべてを見て、
            # j番目のサイコロを0なら反転させる
            temp = []
            c_dice = dice[i] 
            for jj in range(N): # bit
                if (j >> jj) & 1 :
                    c_dice[jj]
            for kk in range(N): # 4進数
                if (k >> kk):
                    
            for ll in range(N):




                    
                    
            


######################################################

if __name__ == "__main__":
    main()