from dataclasses import dataclass
@dataclass
class Game():
    player1: str
    player2: str
    cells: list
game = Game("X","O", ["0","1","2","3","4","5","6","7","8"])
firstInit = True
numOfCells = 8
def GUI():
    print(f"{game.cells[0]} || {game.cells[1]} || {game.cells[2]}")
    print(f"{game.cells[3]} || {game.cells[4]} || {game.cells[5]}")
    print(f"{game.cells[6]} || {game.cells[7]} || {game.cells[8]}")
GUI()
def checkCell():
    global numOfCells
    if numOfCells > 0:
        numOfCells -= 1
        if (game.cells[0] == game.cells[1] == game.cells[2]) or (game.cells[3] == game.cells[4] == game.cells[5]) or (game.cells[6] == game.cells[7] == game.cells[8]) or (game.cells[0] == game.cells[4] == game.cells[8]) or (game.cells[2] == game.cells[4] == game.cells[6]) or (game.cells[0] == game.cells[3] == game.cells[6]) or (game.cells[1] == game.cells[4] == game.cells[7]) or (game.cells[2] == game.cells[5] == game.cells[8]):
            return True
        return False
    else:
        print("it's a draw!")
        return False
while True:
    p1c = int(input("Player 1 choose a cell: "))
    while game.cells[p1c] != game.player1: 
        if(firstInit == False and p2c == p1c):
            print("that cell is occupied!")
            p1c = int(input("Player 1 choose a cell: "))
        else:
            game.cells[p1c] = game.player1
            GUI()
            if checkCell():
                print("Player 1 won!")
                break
    p2c = int(input("Player 2 choose a cell: "))
    while game.cells[p2c] != game.player2: 
        if(p1c == p2c):
            print("that cell is occupied!")
            p2c = int(input("Player 2 choose a cell: "))
        else:
            game.cells[p2c] = game.player2
            firstInit = False
            GUI()
            if checkCell():
                print("Player 2 won!")
                break