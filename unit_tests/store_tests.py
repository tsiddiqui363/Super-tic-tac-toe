import unittest
from game_store import *
import os

from modules.store import save_user, load_user, load_game, save_game


class TestStore(unittest.TestCase):

    def test_save_and_load_game(self):
        # Create a dummy game object
        class DummyGame:
            def __init__(self):
                self.gameID = 123
                self.player1 = 'Alice'
                self.player2 = 'Bob'
                self.gameState = 'In Progress'
                self.history = ['Move 1', 'Move 2']

        game = DummyGame()

        # Save the game
        save_game(game)

        # Check if the file exists
        self.assertTrue(os.path.exists('game_123.json'))

        # Load the game
        loaded_game = DummyGame()
        load_game(loaded_game, 123)

        # Check if the loaded game attributes match the original game
        self.assertEqual(loaded_game.gameID, 123)
        self.assertEqual(loaded_game.player1, 'Alice')
        self.assertEqual(loaded_game.player2, 'Bob')
        self.assertEqual(loaded_game.gameState, 'In Progress')
        self.assertEqual(loaded_game.history, ['Move 1', 'Move 2'])

        # Clean up
        os.remove('game_123.json')

    def test_save_and_load_user(self):
        # Dummy user data
        user_data = {'username': 'Alice', 'score': 100}

        # Save the user data
        save_user(user_data)

        # Check if the file exists
        self.assertTrue(os.path.exists('user_store.json'))

        # Load the user data
        loaded_user_data = load_user('Alice')

        # Check if the loaded user data matches the original user data
        self.assertEqual(loaded_user_data, user_data)

        # Clean up
        os.remove('user_store.json')

if __name__ == '__main__':
    unittest.main()
