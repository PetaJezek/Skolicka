matrix = input().split()
n = len(matrix)
for i in range(len(matrix) - 1):
    newRow = input().split()
    for j in newRow:
        matrix.append(j)
lists = [[] for i in range(2*n + 2)]
matrix = list(map(int,matrix))


for i in range(n):
    for j in range(n):
        lists[i].append(matrix[j + i*n])
for i in range(n):
    for j in range(n):
        lists[i+n].append(matrix[i + n*j])
for i in range(n):
    lists[-2].append(matrix[i + n*i])
for i in range(n):
    lists[-1].append(matrix[n-i- 1 + n * i])
#print(sums)

def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

listsWithZero = []
for i in lists:
    if 0 in i:
        listsWithZero.append(i)

possible = True
if len(listsWithZero) == 3:
    if sum(listsWithZero[0]) ==  sum(listsWithZero[1]) == sum(listsWithZero[2]):
        pass
    else:
        possible = False
else:
    if sum(listsWithZero[0]) ==  sum(listsWithZero[1]):
        pass
    else:
        possible = False
sumarum = 0
for i in lists:
    if sumarum != 0 and sum(i) != sumarum and 0 not in i:
        possible = False
    if 0 not in i:
        sumarum = sum(i)
    

if possible == True:
    add = 0
    for l in lists:
        if sum(l) == sumarum:
            pass
        elif 0 in l:
            if add == 0:
                add = sumarum - sum(l)
                l[l.index(0)] = add
            elif sum(l) + add == sumarum:
                l[l.index(0)] = add
            else:
                possible = False
if possible == True:
    for i in range(n):   
        print(' '.join(map(str, lists[i])))
else: print("Can't be magic")
