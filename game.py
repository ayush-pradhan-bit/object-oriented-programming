
# =============================================================================
# ADD DEFINITION FOR CLASS GAME
# =============================================================================

    '''
    Simple game of TicTacToe (three-in-a-row)
    checking against binary presentation of gameboard,
    static strategy
    '''
    #gameboard winning combinations, common to all objects
    wplaces =  [int('111000000', 2),
                int('000111000', 2),
                int('000000111', 2),
                int('100100100', 2),
                int('010010010', 2),
                int('001001001', 2),
                int('100010001', 2),
                int('001010100',2)]
    #static strategy moves, common to all objects
    bestmoves = (4, 0, 2, 6, 8, 1, 3, 5, 7)                       
        
    def check(self, turn : str):
        '''checks if player in turn won'''
        result = False
        test = (*['1' if x == turn else '0' for x in self.places],)
        for i in range(len(Game.wplaces)):
            if (Game.wplaces[i] & int(''.join(test), 2)) == Game.wplaces[i] : 
                result = True
        return result        
# =============================================================================
# ADD OTHER METHODS 
# =============================================================================
