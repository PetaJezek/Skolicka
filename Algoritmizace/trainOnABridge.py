import queue
import sys

q = queue.Queue()
bridge_length, weigh_limit = (tuple(map(int,input().split())))
train = 0
length = 0
length_of_first = 0
for lines in sys.stdin:
    numbers = list(map(tuple,lines.split()))
    pairs = []
    for i in range(0,len(numbers),2):
        pairs.append(numbers[i],numbers[i+1])
    read = 0
    while read < len(pairs):
        q.put(pairs[read])
        length += pairs[read][0]
        

    


        

        

        
    







