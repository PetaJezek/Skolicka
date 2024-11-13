import heapq

lana = [1,2,3,4,5]

heapq.heapify(lana)
while len(lana) != 1:
    lana[1] = lana[0] + lana[1]
    lana = lana[1:]
    heapq.heapify(lana)
print(lana[0])