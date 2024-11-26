def check():
    n = int(input())
    return _check(n, 0, 0)
def _check(n: int, open: int, close: int):
    if close == n and open == n:
        return 1
    return (_check(n, open + 1, close) if open < n else 0) + (_check(n, open, close + 1) if close < open else 0) 
    
print(check())