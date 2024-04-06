import unittest
from unittest.mock import patch, MagicMock, ANY
from bottle import template
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import serverAPI

class TestGameAPI(unittest.TestCase):

    def setUp(self):
        self.app = serverAPI.GameAPI()
        self.app.user_data = MagicMock()
        self.app.game_sessions = {}

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_register_player_success(self, mock_template, mock_request):
        mock_request.forms.get.side_effect = lambda x: 'testuser' if x == 'username' else 'testpass'
        self.app.user_data.register_player.return_value = True
        self.app.register_player()
        mock_template.assert_called_with('logged_in', message='Please enter a game number to join an existing game, or start a new game.', name='testuser', username='testuser')

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_register_player_failure_existing_user(self, mock_template, mock_request):
        mock_request.forms.get.side_effect = lambda x: 'existinguser' if x == 'username' else 'password'
        self.app.user_data.register_player.return_value = False
        self.app.register_player()
        mock_template.assert_called_with('player_registration.tpl', message="This Username already exists, please try another one!")

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_login_success(self, mock_template, mock_request):
        mock_request.forms.get.side_effect = lambda x: 'testuser' if x == 'username' else 'testpass'
        self.app.user_data.login_player.return_value = True
        self.app.login()
        mock_template.assert_called_with('logged_in', message='Please enter a game number to join an existing game, or start a new game.', name='testuser', username='testuser')

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_login_failure_incorrect_credentials(self, mock_template, mock_request):
        mock_request.forms.get.side_effect = lambda x: 'user' if x == 'username' else 'wrongpass'
        self.app.user_data.login_player.return_value = False
        self.app.login()
        mock_template.assert_called_with('login_page.tpl', message="Your Username or Password doesn't exist. Please try again!")

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_start_game_success(self, mock_template, mock_request):
        mock_request.forms.get.side_effect = lambda x: 'newgame' if x == 'gameID' else 'player1'
        self.app.start_game()
        mock_template.assert_called_with('lobby', username='player1', game_id='newgame')

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_start_game_already_exists(self, mock_template, mock_request):
        game_mock = MagicMock()
        self.app.game_sessions['existinggame'] = {'game': game_mock, 'status': 'active', 'player1': 'player1', 'player2': 'player2', 'updated': {'player1': True}}
        mock_request.forms.get.side_effect = lambda x: 'existinggame' if x == 'gameID' else 'player1'
        self.app.start_game()
        mock_template.assert_called_with('logged_in', message="This Game is already in session, please try another number!", name="", username='player1')

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_join_game_success(self, mock_template, mock_request):
        mock_request.forms.get.side_effect = lambda x: 'existinggame' if x == 'gameID' else 'player2'
        self.app.game_sessions['existinggame'] = {'game': MagicMock(), 'status': 'waiting', 'player1': 'player1', 'async': False, 'updated': {}, 'chat_messages': []}
        self.app.join_game()
        self.assertTrue('player2' in self.app.game_sessions['existinggame'])

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_join_game_full(self, mock_template, mock_request):
        mock_request.forms.get.side_effect = lambda x: 'player3' if x == 'username' else 'fullgame' if x == 'gameID' else None
        self.app.game_sessions['fullgame'] = {
            'game': MagicMock(),
            'status': 'active',
            'player1': 'player1',
            'player2': 'player2',
            'updated': {'player1': False, 'player2': False},
            'chat_messages': []
        }
        self.app.join_game()
        mock_template.assert_called_with('logged_in', message="Game is already full or in progress.", name='player3', username='player3')

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_game_board_invalid_game_id(self, mock_template, mock_request):
        mock_request.query.gameID = 'invalid_game_id'
        mock_request.query.username = 'testuser'
        self.app.game_board()
        mock_template.assert_called_with('error_template.tpl', message="Invalid game ID.", username='testuser')

    @patch('serverAPI.request')
    def test_check_player_joined_true(self, mock_request):
        mock_request.query.username = 'testuser1'
        mock_request.query.gameID = '1'
        self.app.game_sessions['1'] = {
            'game': MagicMock(),
            'status': 'active',
            'player1': 'testuser1',
            'player2': 'testuser2',
            'updated': {'testuser1': False, 'testuser2': False}
        }
        response = self.app.check_player_joined()
        self.assertTrue(response['playerJoined'])

    @patch('serverAPI.request')
    def test_check_game_and_player_status_active_game(self, mock_request):
        mock_request.query.gameID = 'game1'
        mock_request.query.username = 'player1'
        game_mock = MagicMock()
        game_mock.gameState = [1, None]
        self.app.game_sessions['game1'] = {'game': game_mock, 'status': 'active', 'player1': 'player1', 'updated': {'player1': True}}
        response = self.app.check_game_and_player_status()
        self.assertTrue(response['update'])

    @patch('serverAPI.request')
    def test_check_game_and_player_status_no_game_found(self, mock_request):
        mock_request.query.gameID = 'nonexistentgame'
        mock_request.query.username = 'player1'
        response = self.app.check_game_and_player_status()
        self.assertEqual(response, {"error": "Game not found", "update": False})

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_make_move_success(self, mock_template, mock_request):
        mock_request.forms.get.side_effect = lambda x: 'player1' if x == 'username' else 'game1' if x == 'gameID' else '0_0'
        game_mock = MagicMock()
        self.app.game_sessions['game1'] = {'game': game_mock, 'status': 'active', 'player1': 'player1', 'async': False, 'updated': {'player1': False}, 'chat_messages': []}
        self.app.make_move()
        game_mock.play.assert_called_once_with(0, 0)
        self.assertTrue(self.app.game_sessions['game1']['updated']['player1'])

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_make_move_invalid_game_id(self, mock_template, mock_request):
        mock_request.forms.get.side_effect = lambda x: 'player1' if x == 'username' else 'invalidgame' if x == 'gameID' else '0_0'
        self.app.make_move()
        mock_template.assert_called_with('error_template.tpl', message="This game does not exist.", username='player1')

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_game_board_valid_game_id(self, mock_template, mock_request):
        self.app.game_sessions['valid_game_id'] = {'game': MagicMock(gameState=[1, None]), 'chat_messages': [], 'player1': 'testuser', 'updated': {'testuser': False}}
        mock_request.query.gameID = 'valid_game_id'
        mock_request.query.username = 'testuser'
        self.app.game_board()
        mock_template.assert_called_with('game_board.tpl', game_state=ANY, game=ANY, message=ANY, username='testuser', chat_messages=[])

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_post_chat_message_success(self, mock_template, mock_request):
        mock_request.forms.get.side_effect = lambda x: 'testuser' if x == 'username' else 'valid_game_id' if x == 'gameID' else 'Hello World'
        self.app.game_sessions['valid_game_id'] = {'game': MagicMock(), 'chat_messages': [], 'updated': {'testuser': False}}
        self.app.post_chat_message()
        self.assertEqual(self.app.game_sessions['valid_game_id']['chat_messages'], ['testuser: Hello World'])

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_end_game(self, mock_template, mock_request):
        mock_request.forms.get.return_value = 'testuser'
        self.app.game_sessions['game_id'] = {'game': MagicMock(), 'chat_messages': []}
        self.app.end_game('testuser won!', 'testuser', 'game_id')
        mock_template.assert_called_with('end_game', message='testuser won!', username='testuser')

    @patch('serverAPI.request')
    @patch('serverAPI.template')
    def test_user_history_success(self, mock_template, mock_request):
        mock_request.forms.get.return_value = 'testuser'
        self.app.user_data.get_user_history.return_value = [{'gameID': 'game1', 'winStatus': 'Won'}]
        self.app.user_history()
        mock_template.assert_called_with('user_history_page', username='testuser', user_games=[{'gameID': 'game1', 'winStatus': 'Won'}])



if __name__ == '__main__':
    unittest.main()
