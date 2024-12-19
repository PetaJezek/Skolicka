from collections import deque


class Tile:
    def __init__(self, i, j, k, state):
        self.state = state
        self.id = i
        self.row = j
        self.col = k
        self.found = False

start = None
end = None
q = deque()
state_board = []
for i in range(8):
    s = input()
    for j in range(8):
        if s[j] == 'v':
            start = Tile(i*8+j,i,j,0)
            start.found = True
            state_board.append(start)
            q.append(start)
            
        elif s[j] == 'x':
            state_board.append(Tile(i*8+j,i,j,(-2)))

        elif s[j] == 'c':
            end = Tile(i*8+j,i,j,-1)
            state_board.append(end)
        else:
            state_board.append(Tile(i*8+j,i,j,0))
            
while q and end.state == -1:
    loc_tile = q.popleft()
    for i in range(1, 8 - loc_tile.col):
        if i + loc_tile.col > 7:
            break
        if (state_board[i + loc_tile.id]).state == -2:
            break
        if state_board[loc_tile.id + i].state <= 0:
            state_board[i + loc_tile.id].state = loc_tile.state + 1
            q.append(state_board[i + loc_tile.id])
    for i in range(1, loc_tile.col+1):
        if loc_tile.id - i < 0:
            break
        if state_board[loc_tile.id - i].state == -2:
            break
        if state_board[loc_tile.id - i].state <= 0:
            state_board[loc_tile.id - i].state = loc_tile.state + 1
            q.append(state_board[loc_tile.id - i])
    for i in range(1, 8 - loc_tile.row ):
        if loc_tile.row + i > 7:
            break
        if state_board[loc_tile.id + 8*i].state == -2:
            break
        if state_board[loc_tile.id + 8*i].state <= 0:
            state_board[loc_tile.id + 8*i].state = loc_tile.state + 1
            q.append(state_board[loc_tile.id + 8*i])
    for i in range(1, loc_tile.row + 1):
        if loc_tile.row - i < 0:
            break
        if state_board[loc_tile.id - 8*i].state == -2:
            break
        if state_board[loc_tile.id - 8*i].state <= 0:
            state_board[loc_tile.id - 8*i].state = loc_tile.state + 1
            q.append(state_board[loc_tile.id - 8*i]) 
    
print(end.state)
        
        
        




