from unittest import TestCase
from modules.applogic import Game

class TestGame(TestCase):
    def setUp(self):
        self.game = Game("player1")
        self.game.join("player2",self.game.gameID)

    def test_play(self):
        if self.game.currentPlayer == "player1":
            self.game.play(1,1)
            self.assertEquals(self.game.currentPlayer, "player2")
        else:
            self.game.play(1, 1)
            self.assertEquals(self.game.currentPlayer, "player1")

    def test_play_error(self):
        self.assertRaises(IOError, self.game.play(9,9))

    def test_load(self):
        newgame = Game("test")
        newgame.load(self.game.gameID)
        self.assertEquals(newgame.gameID, self.game.gameID)

    def test_load_error(self):
        self.assertRaises(IOError, self.game.load("not a game"))

    def test_join(self):
        newgame = Game("player1")
        newgame.join("player2", newgame.gameID)
        self.assertEquals(newgame.player2, "player2")

    def test_join_error(self):
        self.assertRaises(IOError, self.game.join("testplayer","not a game"))
