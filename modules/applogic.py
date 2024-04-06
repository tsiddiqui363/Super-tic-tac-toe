from random import randint
from modules.store import save_game, load_game

class Game:
    """Game of ultimate tic-tac-toe. Initializes in waiting state.

    Args:
        player_name (str): name of player
        gameID (str): ID of game. Randomized if none is provided
    """

    def __init__(self, player_name, gameID=None):
            
        if(gameID == None):
            gameID = ""
            x = 0
            while x < 10:
                char = randint(0,2)
                if char == 0:
                    char = str(randint(0,9))
                elif char == 1:
                    char = randint(65,90)
                    char = chr(char)
                else:
                    char = randint(97,122)
                    char = chr(char)
                gameID = gameID + char
                x += 1

        self.gameID = gameID
        self.player1 = player_name
        self.player2 = None
        self.gameState = [0,[[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "]],
                        [" "," "," "," "," "," "," "," "," "]]
        self.history = []


    def play(self, board, space):
        """Plays on given board and space. Assumes current player is playing. Saves after play

        Args:
            board (int): number between 0-8 representing what board to play on
            space (int): number between 0-8 representing what space in the board to play on

        Returns:
            Game: self

        Raises:
            IOError if board or space is out of bounds
        """
        #check bounds
        if board > 8 or board < 0:
            raise IOError
        elif space > 8 or space < 0:
            raise IOError
        
        else:
            self.history.append(self.gameState)
            if self.gameState[0] == 1:
                piece = "X"
                nextPlayer = 2
            else:
                piece = "O"
                nextPlayer = 1

            self.gameState[1][board][space] = piece

            #check for win
            if _checkWin(self.gameState[1][board]):
                self.gameState[2][board] = piece
                if _checkWin(self.gameState[2]):
                    self.gameState[0] += 2
                    save_game(self)
                    return self
            #check for tie
            if _checkTie(self.gameState):
                self.gameState[0] = 5
                save_game(self)
                return self

            self.gameState[0] = nextPlayer
            save_game(self)
            return self

    def load(self, gameID=None):
        """Loads game from storage

        Args:
            gameID (str): ID for game to load. Uses game's gameID if none provided

        Returns:
            Bool: True if game can be loaded, else False
        """
        if gameID == None:
            gameID = self.gameID
        return load_game(self,gameID)

    
    def join(self, player2):
        """Joins and starts game in waiting

        Args:
            player2 (str): Name of second player

        Returns:
            Game: self
        """
        self.player2 = player2
        self.history.append(self.gameState)
        turn = randint(1,2)
        self.gameState = [turn,[[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "]],
                        [" "," "," "," "," "," "," "," "," "]]
        return self
        
def _checkWin(board):
    #check horizontals
    for space in [1,4,7]:
        if board[space] != " ":
            if board[space+1] == board[space] and board[space-1] == board[space]:
                return True
            
    #check verticals
    for space in [3,4,5]:
        if board[space] != " ":
            if board[space+3] == board[space] and board[space-3] == board[space]:
                return True
            
    #check diagonalS
    if board[4] != " ":
        if board[0] == board[4] and board[8] == board[4]:
            return True
        if board[2] == board[4] and board[6] == board[4]:
            return True
        
    return False

def _checkTie(state):
    tie = True
    for board in range(0,9):
        if state[2][board] == " ":
            for space in state[1][board]:
                if space == " ":
                    tie = False
    return tie
