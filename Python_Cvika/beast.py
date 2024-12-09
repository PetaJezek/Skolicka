import sys
class Game:
    def __init__(self) -> None:
        self.rounds = int(input())
        #self.grid = [list(line.strip()) for line in sys.stdin]
        self.grid = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
   ['X', '.', '.', '.', '.', 'X', '.', '.', '.', 'X'],
    ['X', '.', '.', '.', '.', 'X', '.', '.', '.', 'X'],
    ['X', '.', 'X', '.', '.', 'X', '.', 'X', '.', 'X'],
    ['X', '.', 'X', '.', '.', '.', '^', 'X', '.', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]
        self.b = Beast(self.grid)
        self.run()
        
    def run(self):
        if self.rounds == 0:
            pass
        else:
            self.move()
            self.run()
    def view(self):
        for i in self.grid:
            print(*i,sep="")
        print("")
    def move(self):
        if self.grid[self.b.pos[0] + self.b.right[0]][self.b.pos[1] + self.b.right[1]] == '.':
            self.b.rotateRight()
            self.grid[self.b.pos[0]][self.b.pos[1]] = self.b.char
            self.view()
            self.rounds -= 1
            if self.rounds > 0:
                self.grid[self.b.pos[0]][self.b.pos[1]] = '.'
                self.b.pos[0] += self.b.forward[0]
                self.b.pos[1] += self.b.forward[1]
                self.grid[self.b.pos[0]][self.b.pos[1]] = self.b.char
                self.view()
                self.rounds -= 1
        elif self.grid[self.b.pos[0] + self.b.right[0]] [self.b.pos[1] + self.b.right[1]] == 'X'\
            and self.grid[self.b.pos[0] + self.b.forward[0]][self.b.pos[1] + self.b.forward[1]] == '.':
            self.grid[self.b.pos[0]][self.b.pos[1]] = '.'
            self.b.pos[0] += self.b.forward[0]
            self.b.pos[1] += self.b.forward[1]
            self.grid[self.b.pos[0]][self.b.pos[1]] = self.b.char
            self.rounds -= 1
            self.view()
        else:
            self.b.rotateLeft()
            self.grid[self.b.pos[0]][self.b.pos[1]] = self.b.char
            self.rounds -= 1
            self.view()
    

class Beast:
    def __init__(self, grid) -> None:
        self.char = '^'
        self.right = [0,0]
        self.forward = [0,0]
        self.left = [0,0]
        self.down = [0,0]
        self.pos = [0,0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =='^':
                    self.char = '^'
                    self.right = [0,1]
                    self.forward = [-1,0]
                    self.left = [0,-1]
                    self.down = [1,0]
                    self.pos = [i,j]
                    break
                elif grid[i][j] =='v':
                    self.char = 'v'
                    self.right = [0,-1]
                    self.forward = [1,0]
                    self.left = [0,1]
                    self.down = [-1,0]
                    self.pos = [i,j]
                    break
                elif grid[i][j] =='>':
                    self.char = '>'
                    self.right = [1,0]
                    self.forward = [0,1]
                    self.left = [-1,0]
                    self.down = [0,-1]
                    self.pos = [i,j]
                    break
                elif grid[i][j] =='<':
                    self.char = '<'
                    self.right = [-1,0]
                    self.forward = [0,-1]
                    self.left = [1,0]
                    self.down = [0,1]
                    self.pos = [i,j]
                    break
    def rotateLeft(self):
        tempVector = self.forward
        self.forward = self.left
        self.left = self.down
        self.down = self.right
        self.right = tempVector 
        if self.char == '^':
            self.char = '<'
        elif self.char == '>':
            self.char = '^'
        elif self.char == 'v':
            self.char = '>'
        else:
            self.char = 'v'
    def rotateRight(self):
        tempVector = self.forward
        self.forward = self.right
        self.right = self.down
        self.down = self.left
        self.left = tempVector
        if self.char == '^':
            self.char = '>'
        elif self.char == '>':
            self.char = 'v'
        elif self.char == 'v':
            self.char = '<'
        else:
            self.char = '^'


g = Game()


