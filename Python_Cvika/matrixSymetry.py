symDiaMain = True
symDiaMin = True
symCenter = True
matrix = []
firstRow = input().split()
n = len(firstRow)
matrix.append(firstRow)

for i in range(n- 1):
    newRow = input().split()
    matrix.append(newRow)

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            symDiaMain = False
            break
    if not symDiaMain:
        break

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
            symDiaMin = False
        if not symDiaMin:
            break
        
for i in range(n//2):
    for j in range(n):
        if matrix[i][j] != matrix[i][n - 1 -j]:
            symCenter = False
    if symCenter == False:
        break
result = []
if symDiaMain == True:
    result.append(1)
else:
    result.append(0)
if symDiaMin == True:
    result.append(1)
else:
    result.append(0)
if symCenter == True:
    result.append(1)
else:
    result.append(0)
print(*result)