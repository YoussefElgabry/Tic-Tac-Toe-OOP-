class Player:
    def __init__(self):
        self.name = " "
        self.symbol = " "
        
    def choose_name(self):
        while True:
            name = input ("Please enter your name (Name only contain letters): ")
            if name.isalpha():
                self.name = name.capitalize()
                break
            print ("Invalid name, Please use letters only!")
            
    def choose_symbol(self):
        #symbol = input (f"{self.name}, choose your symbol (X or O): ")
        while True:
            symbol = input (f"{self.name}, choose your symbol (X or O): ").upper()
            if symbol in ['X', 'O']:
                self.symbol = symbol
                break
            print ("Invalid symbol, Please enter (X or O)!")