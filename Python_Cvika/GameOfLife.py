import copy
rozmer = list(map(int, (input().split())))
steps = int(input())
width = rozmer[0]
height = rozmer[1]
game = [[] for _ in range(height)]
for i in range(height):
    game[i] = list(input())

def CheckniSousedy():
    global game
    game_copy = copy.deepcopy(game)
    for i in range(height):
        for j in range(width):
            left = j - 1
            right = j + 1
            up = i-1
            down = i + 1
            if left <0:
                left = width - 1
            if right >= width:
                right = 0
            if up < 0:
                up = height - 1
            if down >= height:
                down = 0
            vectors = [(up, left), (up, j), (up, right), (i, left), (i, right), (down, left), (down, j), (down, right)]
            dead = 0
            alive = 0
            for h in vectors:
                y = h[0]
                x = h[1]
                if game[y][x] == 'o':
                    alive += 1
                else: dead += 1
            if alive < 2 and game[i][j] == 'o':
                game_copy[i][j] = '.'
            elif alive < 4 and game[i][j] == 'o':
                pass
            elif alive > 3 and game[i][j] == 'o':
                game_copy[i][j] = '.'
            elif alive == 3 and game[i][j] == '.':
                game_copy[i][j] = 'o'
    game = game_copy
    return game


for i in range(steps):
    print("="*width)
    CheckniSousedy()
    for j in range(height):
        print(''.join(game[j]))




                




    