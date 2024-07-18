class Menu:
    def display_main_menu(self):
        print ("Welcome to my X-O game!")
        print ("Choose an option from the following menu")
        print ("1. Start Game")
        print ("2. Exit Game")    
        while True:  
            choice = int (input ("Please Enter Your Choice(1 or 2): "))
            if choice not in [1, 2]:
                print("Invalid Choice, Please enter a valid choice (1 or 2)!")
                continue
            return choice
            break

    
    def endGame_menu(self, winner):
        if winner == 'draw':
            print("The game ended in a draw!")
        
        else:
            print (f"Congratulations {winner}! you won this game!")
        
        print ("""
               Game Over!
               1. Start A New Game
               2. Exit Game
               Please Enter your choice!
               """)
        while True:  
            choice = int (input ("Please Enter Your Choice(1 or 2): "))
            if choice not in [1, 2]:
                print("Invalid Choice, Please enter a valid choice (1 or 2)!")
                continue
            return choice
            break