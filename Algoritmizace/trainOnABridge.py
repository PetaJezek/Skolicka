from collections import deque
import sys

q = deque()
bridge_length, weigh_limit = (tuple(map(int,input().split())))
train = 0
length = 0
length_of_first = 0
weight = 0
Broke = False
for lines in sys.stdin:
    numbers = list(map(int,lines.split()))
    pairs = []
    for i in range(0,len(numbers),2):
        pairs.append((numbers[i],numbers[i+1]))
    read = 0
    while read < len(pairs):
        while bridge_length + length_of_first <= length:
            deleted_train = q.popleft()
            length -= deleted_train[0]
            weight -= deleted_train[1]
            if q:
                length_of_first = q[0][0]
            else:
                length_of_first = 0
        q.append(pairs[read])
        length += pairs[read][0]
        weight += pairs[read][1]
        train += 1
        
        if length_of_first == 0:
            length_of_first = pairs[read][0]
        read +=1
        if weight > weigh_limit:
            print(train)
            Broke = True
            break
    if Broke:
        break   
if not Broke:
    print(-1)
        

    


        

        

        
    







