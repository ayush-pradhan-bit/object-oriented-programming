import tkinter as tk
from game import Game
    
        
class TicTacToe(tk.Tk) :
    '''GUI for TicTacToe, has Game as an attribute'''
        
    def __init__(self, name=str(), *args, **kwargs) :
        '''creates 9 buttons in a loop'''
        super().__init__(*args, **kwargs) #call Tk class initializer
        self.title('Naughts and crosses')
        self.geometry('300x300')
        self.__game = Game()
        self.__content = [0]*9  
        self.__moves = 0
# =============================================================================
#         DD DESERIALIZATION (PICKLE) AND RESTORE UI
# =============================================================================

        for i in range(9): 
            self.__content[i] = tk.Button(self, text=' ', width = 10, height = 5, command = lambda i = i: self.move(i) )
            self.__content[i].grid(row = i // 3, column = i % 3, padx = 5, pady = 5, sticky = tk.E + tk.W+ tk.N + tk.S)
            self.rowconfigure(i // 3, weight = 1)
            self.columnconfigure(i % 3, weight = 1)  
            
        self.protocol("WM_DELETE_WINDOW", self.__delete_window)    
    
    def move(self, id):
        '''user move, check if win or draw, machine move, check if lose'''
        if self.__game.usermove(id):
            self.__content[id].config(text = 'X')
            self.__moves += 1 
            if self.__game.check('X') and self.__moves > 4 :
                self.showresult('X')
            elif self.__moves == 9: 
                self.showresult('Draw')                
            else:
                self.__content[self.__game.machinemove()].config(text = 'O')
                self.__moves += 1 
                if self.__game.check('O') and self.__moves > 4 :
                    self.showresult('O')
     
    def showresult(self, turn):
        '''check is either wins and ask if user wants a new game'''  
        title = f'{turn} wins!' if turn != 'Draw' else f"it's a {turn}"
        if tk.messagebox.askyesno(title, 'Start a new game?'):
            self.reset()
        else : 
            self.__delete_window()               
       
    def reset(self):
        '''reset game, buttons and moves'''
        self.__game.reset()
        for i in range(9): 
            self.__content[i].config(text = ' ')
        self.__moves = 0       

    def __delete_window(self):
        title = 'Game has not ended yet' 
        if tk.messagebox.askyesno(title, 'Do you really want to close the game?'):
# =============================================================================
#             ADD SERIALIZATION (PICKLE)
# =============================================================================
            self.destroy()
        else:
            pass 
     
if __name__ == '__main__' :

    ttt = TicTacToe()
    ttt.mainloop()
    




    

