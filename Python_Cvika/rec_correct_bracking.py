
def check():
    n = int(input())
    return _check(n, 0, 0)
def _check(n: int, open: int, close: int):
    if close == n and open == n:
        return 1
    if open > n or close > open:
        return 0
    add_open = _check(n, open + 1, close) if open < n else 0
    add_close = _check(n, open, close + 1) if close < open else 0
    return add_open + add_close
print(check())