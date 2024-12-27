def Solve():
    def _Solve(cur_coins: list):
        sumarum = sum(cur_coins)
        if sum(cur_coins) > cap:
            return
        if sum(cur_coins) == cap:
            print(*cur_coins)
            return
        for i in coins:
            if i <= cur_coins[-1] and sum(cur_coins) + i <= cap:
                cur_coins.append(i)
                _Solve(cur_coins)
                cur_coins.pop() ## Napad nalezen na internetu: backtrack
    
    count = int(input())
    coins = list(map(int,input().split()))
    cap = int(input())
    
    for i in coins:
        a = [i]
        _Solve(a)
    
 
Solve()        
        