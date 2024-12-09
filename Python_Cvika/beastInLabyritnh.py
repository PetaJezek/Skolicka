import sys

class Map:
    grid = []

    def __init__(self):
        n = int(input())
        global grid
        ##grid = [line.strip() for line in sys.stdin.readlines()]
        grid = [
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
            ['X', '.', '.', '.', '.', 'X', '.', '.', '.', 'X']
            ['X', '.', '.', '.', '.', 'X', '.', '.', '.', 'X']
            ['X', '.', 'X', '.', '.', 'X', '.', 'X', '.', 'X']
            ['X', '.', 'X', '.', '.', '.', '^', 'X', '.', 'X']
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]
        b = Beast(grid)
        self.run(n)
    def run(self, n: int):
        for i in range(n):
            self.move()
            self.view()
    def view():
        pass
    def move():
        pass

class Beast:
    def __init__(self,grid):
        