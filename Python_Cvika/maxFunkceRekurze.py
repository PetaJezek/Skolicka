def max(a,i,j):
    if len(a) == 1:
        return a[0]
    if a[i+1] > a[i]:
        a[:1 ]

def search(a,x,i,j):
    mid =  a[(j+i)//2-1]
    
    if x == mid:
        return True
    if i > j:
        return False
    elif x > mid:
        
        return search(a,x,(j+i)//2 + 1,j)
    else:
        return search(a,x,i,(j+i)//2 -1)
        
    
print(search([1,2,3,4],6,0,4))


def mul(a,b):
    if b>0:
        return a + int(mul(a,b-1))
print(mul(2,3))