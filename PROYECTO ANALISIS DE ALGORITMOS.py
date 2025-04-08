#PROYECTO ANALISIS DE ALGORITMOS
class Mancala:
    def __init__(self):
        # Inicializar el tablero: 6 pozos para cada jugador y 1 mancala
        self.board = [4] * 6 + [0] + [4] * 6 + [0]
        self.player_turn = 1  # Jugador 1 comienza

    def print_board(self):
        print("\nTablero:")
        print("Jugador 2 (Mancala: {})".format(self.board[13]))
        print ("Posicion fichas: 12  11  10  9  8  7")
        print("Pozo jugador 2: ", self.board[12:6:-1])
        print("Pozo jugador 1 ", self.board[0:6])
        print ("Posicion fichas: 0  1  2  3  4  5")
        print("Jugador 1 (Mancala: {})".format(self.board[6]))
        print("Turno del Jugador", self.player_turn)

    def make_move(self, pit):
        if self.player_turn == 1:
            if pit < 0 or pit > 5 or self.board[pit] == 0:
                print("Movimiento inválido. Intenta de nuevo.")
                return False
        else:
            if pit < 7 or pit > 12 or self.board[pit] == 0:
                print("Movimiento inválido. Intenta de nuevo.")
                return False

        stones = self.board[pit]
        self.board[pit] = 0
        current_pit = pit

        while stones > 0:
            current_pit = (current_pit + 1) % 14
            if (self.player_turn == 1 and current_pit == 13) or (self.player_turn == 2 and current_pit == 6):
                continue  # Saltar el mancala del oponente
            self.board[current_pit] += 1
            stones -= 1

        # Captura de piedras
        if self.board[current_pit] == 1 and ((self.player_turn == 1 and 0 <= current_pit <= 5) or (self.player_turn == 2 and 7 <= current_pit <= 12)):
            opposite_pit = 12 - current_pit
            if self.board[opposite_pit] > 0:
                self.board[6 if self.player_turn == 1 else 13] += self.board[opposite_pit] + 1
                self.board[current_pit] = 0
                self.board[opposite_pit] = 0

        # Cambio de turno
        if (self.player_turn == 1 and current_pit != 6) or (self.player_turn == 2 and current_pit != 13):
            self.player_turn = 3 - self.player_turn

        return True

    def check_game_over(self):
        if all(stones == 0 for stones in self.board[0:6]) or all(stones == 0 for stones in self.board[7:13]):
            self.board[6] += sum(self.board[0:6])
            self.board[13] += sum(self.board[7:13])
            for i in range(14):
                if i != 6 and i != 13:
                    self.board[i] = 0
            return True
        return False

    def get_winner(self):
        if self.board[6] > self.board[13]:
            return "Jugador 1"
        elif self.board[6] < self.board[13]:
            return "Jugador 2"
        else:
            return "Empate"

def main():
    game = Mancala()
    while True:
        game.print_board()
        if game.player_turn == 1:
            pit = int(input("Jugador 1, elige un pozo (0-5): "))
        else:
            pit = int(input("Jugador 2, elige un pozo (7-12): "))

        if not game.make_move(pit):
            continue

        if game.check_game_over():
            game.print_board()
            print("¡Juego terminado!")
            print("El ganador es:", game.get_winner())
            break

if __name__ == "__main__":
    main()