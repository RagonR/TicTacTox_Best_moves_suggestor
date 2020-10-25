class TicTacToe:

    def __init__(self):
        self._squares = {}
        self._winningCombos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8], #Is kairės į desine
        [0, 3, 6], [1, 4, 7], [2, 5, 8], #Is virsaus į apačią
        [0, 4, 8], [2, 4, 6]) #Įstrižai

    def createBoard(self):
        for i in range(9):
            self._squares[i] = "."
        print(self._squares)

    def showBoard(self):
        print()
        print(self._squares[0], self._squares[1], self._squares[2])
        print(self._squares[3], self._squares[4], self._squares[5])
        print(self._squares[6], self._squares[7], self._squares[8])

    def getAvailableMoves(self):
        self._availableMoves = []
        for i in range(9) :
            if self._squares[i] == ".":
                self._availableMoves.append(i)
        return self._availableMoves

    def makeMove(self, position, player):
        self._squares[position] = player
        self.showBoard()

    def complete(self):
        if "." not in self._squares.values():
            return True
        if self.getWinner() != None:
            return True
        return False

    def getWinner(self):
        for player in ("x", "o"):
            for combos in self._winningCombos:
                if self._squares[combos[0]] == player and self._squares[combos[1]] == player and self._squares[combos[2]] == player:
                    return player
        if "." not in self._squares.values():
            return "tie"
        return None

    def getEnemyPlayer(self, player):
        if player == "x" :
            return "o"
        return "x"


    def minimax(self, player, depth = 0):
        if player == "o":
            best = -10
        else:
            best = 10
        if self.complete():
            if self.getWinner() == "x":
                return -10 + depth, None
            elif self.getWinner() == "tie":
                return 0, None
            elif self.getWinner() == "o":
                return 10 - depth, None
        for move in self.getAvailableMoves():
            self.makeMove(move, player)
            val, _ = self.minimax(self.getEnemyPlayer(player), depth+1)
            print(val)
            if player == "o":
                if val > best:
                    best, bestMove = val, move
                    if depth == 0:
                        print("Currently best move would be: ", bestMove)
            else:
                if val < best:
                    best, bestMove = val, move
            self.makeMove(move, ".")
        return best, bestMove

def gameStart():
    game = TicTacToe()
    game.createBoard()
    game.makeMove(3, "x")
    game.makeMove(4, "o")
    game.makeMove(5, "x")
    game.makeMove(6, "o")
    game.makeMove(7, "x")
    print("Initial moves done")
    val, bestMove = game.minimax("o")
    print('best move', bestMove)

gameStart()