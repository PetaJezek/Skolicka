def gen_seq(k,s: str, seq, natural_numbers: list):
    if len(s) == k:
        seq.append(s)
        return seq
    for i in range(1, len(natural_numbers) - natural_numbers.index(s[-1])):
        s = s + str(i)
        gen_seq(k, s, seq, natural_numbers)
    return seq
    
def wrapper(k: int, n: int):
    seq = []
    natural_numbers = [str(i + 1) for i in range(n)]
    for i in range(1, n-k+1):
        s = str(i)
        gen_seq(k, s,seq,natural_numbers)
    return seq
print(wrapper(2,3))