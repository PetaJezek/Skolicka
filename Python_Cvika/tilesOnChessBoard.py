n = int(input())
m = int(input())
def Solve(hor_matrix: list, ver_matrix: list):
    solutions = 0
    for i in ver_matrix:
        if len(i) >= n:
            solutions += len(i) + 1 - n
    for j in hor_matrix:
        if len(j) >= n:
            solutions += len(j) + 1 - n
    return solutions

# ver_matrix = []#[] for _ in range (m)]
# hor_metrix = [[] for _ in range(m)]
# for i in range(m):
#     line = list(map(int,(input().split())))
#     cur_list = []
#     for j in range(m):
#         if line[j] == 0:
#             cur_list.append(0)
#         elif line[j] == 1 and cur_list:
#             ver_matrix.append(cur_list)
#             cur_list = []
#     if cur_list:
#         ver_matrix.append(cur_list)
    
#     for g in range(m):
#         hor_metrix[g].append(line[g])
# for i in hor_metrix:
#     while 1 in i:
#         i.remove(1)            
# print(Solve(hor_metrix, ver_matrix))

first = True
while m != 0:
    if not first:
        m = int(input())
    first = False
    ver_matrix = []
    hor_metrix = [[] for _ in range(m)]
    for i in range(m):
        line = list(map(int,(input().split())))
        cur_list = []
        for j in range(m):
            if line[j] == 0:
                cur_list.append(0)
            elif line[j] == 1 and cur_list:
                ver_matrix.append(cur_list)
                cur_list = []
        if cur_list:
            ver_matrix.append(cur_list)
        
        for g in range(m):
            hor_metrix[g].append(line[g])
    horizontal_matrix = []
    for i in hor_metrix:
        curent_sublist = []
        for j in i:
            if j == 0:
                curent_sublist.append(0)
            else:
                if curent_sublist:
                    horizontal_matrix.append(curent_sublist)
                    curent_sublist = []
        if curent_sublist:
            horizontal_matrix.append(curent_sublist)


    if m != 0:
        print(Solve(horizontal_matrix, ver_matrix))
    




