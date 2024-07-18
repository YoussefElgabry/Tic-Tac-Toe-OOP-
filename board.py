class Board:
    def __init__(self):
        self.board = [str(i) for i in range (1,10)]
        
    def display_board(self):
        for i in range (0,9,3):
            print (" | ".join(self.board [i: i+3]))
            if i < 9:
                print ("-" * 10)
                
    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        return False
        
    def reset_board(self):
        self.__init__()
            
    
    def is_valid_move(self, choice):
        return self.board[choice-1].isdigit()