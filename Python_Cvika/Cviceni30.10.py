def findValue(f,k):
    low = -1
    hi = 1
    while f(low) < k and f(hi) > k:
       
        if f(low) > k:
            low = low * 2
        elif f(hi) < k:
            hi = hi * 2

    mid = (low + hi) // 2
    while f(low) < k and f(hi) > k:
        if mid == k:
            return mid
        elif k > mid:
            low = mid +1
        else:
            hi = mid - 1
    
    if f(low) > k:
        return low - 1
    else:
        return hi - 1


    


        

