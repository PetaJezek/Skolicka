import sys
from itertools import permutations 
n = int(input())
tiles = []
eaten_pos = []
for i in range(n):
    tiles.append(list(input()))
    
for i in range(n):
    for j in range(n):
        if tiles[i][j] == 'X':
            eaten_pos.append((i,j))

perms = []
for i in range(1, n+1):
    perms.append(i)
perm = list(permutations(perms))
x = len(perm)

for j in perm:
    for i in eaten_pos:
        if j[i[0]] == i[1]+1:
            x -= 1
            break



print(x)
