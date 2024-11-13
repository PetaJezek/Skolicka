class Matrix():
    def __init__(self, ll):
        self.matrix = ll
    def __str__(self):
        id = 0
        final = ""
        for i in self.matrix:
            id += 1
            line = " ".join(str(i))
            if id < len(self.matrix):
                line += "\n"
            final += line
        return final
        
            

m = Matrix([[1,2,3],[1,2,3]])
print(m)