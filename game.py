import menu
import player
import board
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Game:
    
    def __init__(self):
        self.menu = menu.Menu()
        self.players = [player.Player(), player.Player()]
        self.board = board.Board()
        self.current_player_index = 0
        
    def start_game(self):
        player_choice = self.menu.display_main_menu()
        
        if player_choice == 1:
            self.setup_players()
            self.play_game()
            
        else:
            self.quit_game()
            
    def setup_players(self):
        for number, player in enumerate(self.players, start = 1):
            print (f"player {number}, enter your name & symbol: ")
            player.choose_name()
            player.choose_symbol()
            clear_screen()
            #print ('-' * 20)
            
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.endGame_menu(self.players[1 - self.current_player_index].name)
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break
    
    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn")
        while True:
            try:
                cell_choice = int(input("Chose a cell (1-9)"))
                if 1 <= cell_choice <=9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print('Invalid Move, Try Again!')
            except ValueError:
                print('Please enter a number between 1 and 9.')

        self.switch_player()
        clear_screen()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index         

    def quit_game(self):
        print("Game Over, Thank you for playing!")
        
    def check_win(self):
        winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8],     #row
                   [0, 3, 6], [1, 4, 7], [2, 5, 8],     #columns
                   [0, 4, 8], [2, 4, 6]]                #diagonals
                   
        for w in winning:
            if self.board.board[w[0]] == self.board.board[w[1]] == self.board.board[w[2]]: 
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)
        #this line means that all the cells in the board were filled with symbols without achieving any winning condition

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

Game().start_game()