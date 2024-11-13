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
        m = copy.deepcopy(self)
        for i in range(len(self.matrix)):
            for j in range (len(self.matrix[0])):
                m.matrix[i][j] += mat2.matrix[i][j]
        ##print(m)
        return(m)  
    def __sub__(self,mat2):
        m = copy.deepcopy(self)
        for i in range(len(self.matrix)):
            for j in range (len(self.matrix[0])):
                m.matrix[i][j] -= mat2.matrix[i][j]
        ##print(m)  
        return(m)
    def __mul__(self,scal):
        m = copy.deepcopy(self)
        for i in range(len(self.matrix)):
            for j in range (len(self.matrix[0])):
                m.matrix[i][j] *= scal
        return(m)
    def __rmul__(self, mat2):
        m = copy.deepcopy(self)
        for i in range(len(self.matrix)):
            for j in range (len(self.matrix[0])):
                m.matrix[i][j] = 0
        soucet = 0
        for i in range(len(self.matrix)):
            for j in range (len(self.matrix[0])):
                for k in range(len(self.matrix[0])):
                    soucet += self.matrix[i][k] * mat2.matrix[k][j]
                m.matrix[i][j] = soucet
                soucet = 0
            
                
                
        return(m)
m = Matrix([[2, 3, 4], [5, 6, 7]])
n = Matrix([[1, 2, 3], [2, 3, 4]])

print(m-n)
print(m*n)


