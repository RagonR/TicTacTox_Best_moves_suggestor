class TicTacToe:
    def __init__(self):
        self._squares = {}
        self._winningCombos = (
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontally
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertically
            [0, 4, 8], [2, 4, 6])  # Diagonally

    def create_board(self):
        for i in range(9):
            self._squares[i] = "."
        print(self._squares)

    def show_board(self):
        print()
        print(self._squares[0], self._squares[1], self._squares[2])
        print(self._squares[3], self._squares[4], self._squares[5])
        print(self._squares[6], self._squares[7], self._squares[8])

    def get_available_moves(self):
        self._availableMoves = []
        for i in range(9):
            if self._squares[i] == ".":
                self._availableMoves.append(i)
        return self._availableMoves

    def make_move(self, position, player):
        self._squares[position] = player
        self.show_board()

    def complete(self):
        if "." not in self._squares.values():
            return True
        if self.get_winner() is not None:
            return True
        return False

    def get_winner(self):
        for player in ("x", "o"):
            for combos in self._winningCombos:
                if self._squares[combos[0]] == player and self._squares[combos[1]] == player and self._squares[
                    combos[2]] == player:
                    return player
        if "." not in self._squares.values():
            return "tie"
        return None

    def get_enemy_player(self, player):
        if player == "x":
            return "o"
        return "x"

    def mini_max(self, player, depth=0):
        if player == "o":
            best = -10
        else:
            best = 10
        if self.complete():
            if self.get_winner() == "x":
                return -10 + depth, None
            elif self.get_winner() == "tie":
                return 0, None
            elif self.get_winner() == "o":
                return 10 - depth, None
        for move in self.get_available_moves():
            self.make_move(move, player)
            val, _ = self.mini_max(self.get_enemy_player(player), depth + 1)
            print(val)
            if player == "o":
                if val > best:
                    best, best_move = val, move
                    if depth == 0:
                        print("Currently best move would be: ", best_move)
            else:
                if val < best:
                    best, best_move = val, move
            self.make_move(move, ".")
        return best, best_move


def game_start():
    game = TicTacToe()
    game.create_board()
    game.make_move(3, "x")
    game.make_move(4, "o")
    game.make_move(5, "x")
    game.make_move(6, "o")
    game.make_move(7, "x")
    print("Initial moves done")
    val, best_move = game.mini_max("o")
    print('best move', best_move + 1)


game_start()
