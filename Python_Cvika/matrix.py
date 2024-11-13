import copy
class Matrix():
    def __init__(self, ll):
        self.matrix = ll
    def __repr__(self):
        final = ""
        for i in self.matrix:
            for j in i:
                final += str(j) + ' '
            final = final.strip()
            final += '\n'
        return final.strip()
    def vals(self):
        ##print(self.matrix)
        return(self.matrix)
    def dims(self):       
        r = len(self.matrix)
        c = len(self.matrix[0])
        dimensions = (r,c)
        ##print(dimensions)
        return(dimensions)
    def __add__(self, mat2):
        mat = copy.deepcopy(self)
        for i in range(len(self.matrix)):
            for j in range (len(self.matrix[0])):
                mat.matrix[i][j] += mat2.matrix[i][j]
        ##print(m)
        return(mat)  
    def __sub__(self,mat2):
        mat = copy.deepcopy(self)
        for i in range(len(self.matrix)):
            for j in range (len(self.matrix[0])):
                mat.matrix[i][j] -= mat2.matrix[i][j]
        ##print(m)  
        return(mat)
    def __mul__(self, other):   
        if isinstance(other,(int, float)):
            mat = copy.deepcopy(self)
            for i in range(len(self.matrix)):
                for j in range (len(self.matrix[0])):
                    mat.matrix[i][j] *= other
            return(mat)
        elif isinstance(other, Matrix):
            mat = Matrix([[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))])
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(self.matrix[0])):
                        mat.matrix[i][j] += self.matrix[i][k]*other.matrix[k][j]
            return(mat)
    def is_symmetric(self):
        if(len(self.matrix)== len(self.matrix[0])):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    if self.matrix[i][j] != self.matrix[j][i]:
                        return False
            return True    
        else: return False
    

def zero_matrix(r,c):
    mat = Matrix([[0 for _ in range(c)] for _ in range(r)])
    return mat
def identity_matrix(n):
    mat = Matrix([[0 for _ in range(n)] for _ in range(n)])
    for i in range(n):
        for j in range(n):
            if i==j:
                mat.matrix[i][j] = 1
    return mat
    

#m = Matrix([[2, 3], [6, 7],[5 , 2]])
# n = Matrix([[1, 2, 3], [2, 3, 4]])
# q = Matrix([[1, 2, 2], [2, 3, 4], [3, 4, 5]])

#print(m*5)
# print(m)
# print(q.is_symmetric())
# print(identity_matrix(5))

