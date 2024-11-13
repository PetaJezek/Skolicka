def TiskStromu():
    k = int(input())
    l = int(input())
    for i in range(k):
        print("." * (k-i - 1) + "*" * (1 + 2*i) + "." * (k-i - 1) )
    for i in range(l):
        print("." * (k-1) + "*" + "." * (k-1)) 

TiskStromu()