def cut(s, seq, start, stop):
    
    for i in range(len(s)):
        if s[start:stop] == s[start:stop:-1]:
            seq.append(s[start:stop] + "," + cut(s[stop:],seq, stop, stop+1))
            return seq
        elif stop != len(s):
            seq.append(cut(s[stop:],seq, start, stop+1))
            return seq
def wrap(s):
    
