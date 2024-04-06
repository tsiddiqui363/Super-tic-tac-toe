from bottle import Bottle, request, response, static_file, template, TEMPLATE_PATH
from modules import *
import secrets

from modules.user import User
from modules.applogic import Game

TEMPLATE_PATH.insert(0, './html_template')
host = "localhost"
serverPort = 8080


class GameAPI(Bottle):
    def __init__(self):
        """
        Initializes the GameAPI class and sets up the routes for the game server.

        """
        super().__init__()
        self.route('/', callback=self.serve_homepage)
        self.route('/register_page', callback=self.register_page)
        self.route('/login_page', callback=self.login_page)
        self.route('/register', callback=self.register_player, method='POST')
        self.route('/login', callback=self.login, method='POST')
        self.route('/game', callback=self.login)
        self.route('/start_game', callback=self.start_game, method='POST')
        self.route('/join_game', callback=self.join_game, method='POST')
        self.route('/check_player_joined', callback=self.check_player_joined, method='GET')
        self.route('/check_game_and_player_status', callback=self.check_game_and_player_status, method='GET')
        self.route('/game_board', callback=self.game_board)
        self.route('/make_move', callback=self.make_move, method='POST')
        self.route('/logged_in', callback=self.logged_in, method='POST')
        self.route('/user_history', callback=self.user_history, method='POST')
        self.route('/post_chat_message', callback=self.post_chat_message, method='POST')

        self.user_data = User()
        self.game_sessions = {}
        

    def serve_homepage(self):
        """
        Serves the homepage of the game.

        Returns:
            The homepage template.
        """
        return template('homepage')
    

    def login_page(self):
        """
        Serves the player registration page.

        Returns:
            The login_page template.
        """
        return template('login_page.tpl', message="Please enter your Username and Password to continue")


    def register_page(self):
        """
        Serves the login page.

        Returns:
            The player_registration template.
        """
        return template('player_registration.tpl', message="Please enter your Username and Password to register")


    def register_player(self):
        """
        Registers a new player with the game server.

        Returns:
            A call to the logged_in method if successful or back to the player_registration template if unsuccessful.
        """
        username = request.forms.get('username')
        password = request.forms.get('password')

        registration_status = self.user_data.register_player(username=username, password=password)
        if registration_status == True:
            return self.logged_in(username)
        else:
            return template('player_registration.tpl', message="This Username already exists, please try another one!")


    def login(self):
        """
        Authenticates an already registered player, allowing them to log in to the game server.

        Returns:
            The logged_in template if successful or back to login_page if unsuccessful.
        """
        username = request.forms.get('username')
        password = request.forms.get('password')

        login_status = self.user_data.login_player(username=username, password=password)
        if login_status:
            return self.logged_in(username)
        else:
            return template('login_page.tpl', message="Your Username or Password doesn't exist. Please try again!")
        

    def logged_in(self, username=None):
        """
        Serves the page after a user has logged in, allowing them to join or start a game.

        Returns:
            The logged_in template.
        Serves the page after a User_inter has logged in, allowing them to join or start a game.
        """
        if username is None:
            username = request.forms.get('username')
        return template('logged_in', message="Please enter a game number to join an existing game, or start a new game.", name=username, username=username)


    def start_game(self):
        """
        Starts a new game session on the game server.

        Returns:
            A lobby template where the player waits for the other, or back to logged_in template if the game already exists.
        """
        username = request.forms.get('username')
        game_id = request.forms.get('gameID')

        if game_id in self.game_sessions.keys():
            return template('logged_in', message="This Game is already in session, please try another number!", name="", username=username)
        else:
            game = Game(player_name=username, gameID=game_id)
            self.game_sessions[game_id] = {
                'game': game, 
                'status': 'waiting', 
                'player1': username,
                'updated': {username: False},
                'async': False,
                'chat_messages': []
            }
            return template('lobby', username=username, game_id=game_id)


    def join_game(self):
        """
        Allows the user to join an existing game using the game ID.

        Returns:
            A call to the game_board method if the game was in waiting, or the logged_in template if the game does not exist or is full.
        Allows the User_inter to join an existing game using the game ID.
        """
        username = request.forms.get('username')
        game_id = request.forms.get('gameID') 
        
        if game_id not in self.game_sessions.keys():
            async_game = Game(username)
            if async_game.load(game_id):
                if username == async_game.player1 or username == async_game.player2:
                    #join game
                    self.game_sessions[game_id] = {
                        'game': async_game,
                        'status': 'active',
                        'player1': async_game.player1,
                        'player2': async_game.player2,
                        'updated': {async_game.player1: False, async_game.player2: False},
                        'async': True,
                        'chat_messages': []
                    }
                    return self.game_board(game_id=game_id, username=username)
                else:
                    return template('logged_in', message="You are not a participant of this game!", name=username, username=username)
            return template('logged_in', message="This Game does not exist, please enter a valid Game Number!", name=username, username=username)
        
        if self.game_sessions[game_id]['status'] == 'waiting':
            self.game_sessions[game_id]['player2'] = username
            self.game_sessions[game_id]['updated'][username] = False
            self.game_sessions[game_id]['status'] = 'active'
            self.game_sessions[game_id]['game'].join(username)
            return self.game_board(game_id=game_id, username=username)
        elif self.game_sessions[game_id]['status'] == 'active':
            #join game if already being played async
            if username == self.game_sessions[game_id]['player1'] or username == self.game_sessions[game_id]['player2']:
                self.game_sessions[game_id]['async'] = False
                return self.game_board(game_id=game_id, username=username)
            else:
                return template('logged_in', message="Game is already full or in progress.", name=username, username=username)


    def check_player_joined(self):
        """
        Checks if a player has joined the game.

        Returns:
            A JSON object representing the whether a player joined the game or not.
        """
        username = request.query.username
        game_id = request.query.gameID
        response.content_type = 'application/json'
        game_info = self.game_sessions.get(game_id, None)

        if game_info and username in [game_info.get('player1'), game_info.get('player2')] and game_info['status'] == 'active':
            return {"playerJoined": True, "gameID": game_id}
        return {"playerJoined": False}


    def check_game_and_player_status(self):
        """
        Checks the current status of the game and the player.

        Returns:
            A JSON object representing the update status, current player turn, and win status.
        """
        game_id = request.query.gameID
        username = request.query.username
        game_session = self.game_sessions.get(game_id)
        
        if not game_session:
            return {"error": "Game not found", "update": False}
        
        current_turn_number = game_session['game'].gameState[0]

        update = any(value for value in game_session['updated'].values())
        if current_turn_number == 1 or current_turn_number == 2:
            response = {
                "update": update,
                "currentTurn": game_session[f'player{current_turn_number}'],
                "winner": False
            }
        elif current_turn_number == 3 or current_turn_number == 4:
            response = {
                "update": True,
                "currentTurn": False,
                "winner": game_session[f'player{current_turn_number-2}']
            }
        else:
            response = {
                "update": True,
                "currentTurn": False,
                "winner": "It's a tie!"
            }
        game_session['updated'][username] = False
            
        return response


    def make_move(self):
        """
        Allows a player to make a move in the game session and updates scores accordingly.

        Returns:
            A call to the game board method, after making the move, or an error template if the game id or move is invalid.
        """
        username = request.forms.get('username')
        game_id = request.forms.get('gameID')
        selected_move = request.forms.get('selectedMove')

        if game_id not in self.game_sessions:
            return template('error_template.tpl', message="This game does not exist.", username=username)

        game_session = self.game_sessions[game_id]
        game = game_session['game']

        try:
            board_index, space_index = selected_move.split('_')
            board_index = int(board_index)
            space_index = int(space_index)
            game.play(board_index, space_index)
            if not game_session['async']:  #dont update players if being played async
                for key in game_session['updated'].keys():
                    game_session['updated'][key] = True
            return self.game_board(game_id=game_id, username=username)
        except ValueError:
            return template('error_template.tpl', message="Invalid move format.", username=username)
        except IOError:
            return template('error_template.tpl', message="Invalid move.", username=username)


    def game_board(self, username=None, game_id=None):
        """
        Displays the game board for a specific game session.

        Args:
            username (str, optional): The username of the current player.
            game_id (str, optional): The unique identifier for the game session.

        Returns:
            A template rendering of the game board or an error message if the game ID is invalid or not found.
        """
        if username is None:
            username = request.query.username
        if game_id is None:
            game_id = request.query.gameID
        if not game_id or game_id not in self.game_sessions:
            return template('error_template.tpl', message="Invalid game ID.", username=username)

        chat_messages = self.game_sessions[game_id]['chat_messages']

        game_session = self.game_sessions[game_id]
        if game_session['game'].gameState[0] == 1:
            message = f"It's {game_session['player1']}'s turn (X)"
        elif game_session['game'].gameState[0] == 2:
            message = f"It's {game_session['player2']}'s turn (O)"
        elif game_session['game'].gameState[0] == 3:
            #updates User_inter history
            new_history = self.user_data.get_user_history(username)
            if username == game_session['player1']:
                new_history.append({'gameID': game_id, 'winStatus': "Won"})
            else:
                new_history.append({'gameID': game_id, 'winStatus': "Lost"})
            self.user_data.update_profile(username, {'history': new_history})

            return self.end_game(winner = f"{game_session['player1']} won!", username=username, game_id=game_id)
        elif game_session['game'].gameState[0] == 4:
            #updates User_inter history
            new_history = self.user_data.get_user_history(username)
            if username == game_session['player2']:
                new_history.append({'gameID': game_id, 'winStatus': "Won"})
            else:
                new_history.append({'gameID': game_id, 'winStatus': "Lost"})
            self.user_data.update_profile(username, {'history': new_history})

            return self.end_game(winner = f"{game_session['player2']} won!", username=username, game_id=game_id)
        else:
            #updates User_inter history
            new_history = self.user_data.get_user_history(username)
            new_history.append({'gameID': game_id, 'winStatus': "Tie"})
            self.user_data.update_profile(username, {'history': new_history})

            return self.end_game(winner = f"It's a tie!", username=username, game_id=game_id)
        return template('game_board.tpl', game_state=game_session['game'].gameState[1], game=game_session['game'], message=message, username=username, chat_messages=chat_messages)


    def post_chat_message(self):
        """
        Handles posting a chat message to the game session.

        Returns:
            A call to the game_board with the with the new chat message or an error template if the game id is invalid.
        """
        username = request.forms.get('username')
        game_id = request.forms.get('gameID')
        message = request.forms.get('chat_message')

        if game_id in self.game_sessions:
            chat_message = f"{username}: {message}"
            game_session = self.game_sessions[game_id]
            game_session['chat_messages'].append(chat_message)
            for key in game_session['updated'].keys():
                game_session['updated'][key] = True
            return self.game_board(username=username, game_id=game_id)
        else:
            return template('error_template.tpl', message="Invalid game ID.", username=username)


    def end_game(self, winner, username, game_id):
        """
        Ends the game session, displays the game outcome, and removes the game from the session.

        Args:
            winner (str): The message to display as the outcome of the game.
            username (str): The username of the player who initiated the end game.
            game_id (str): The unique identifier for the game session being ended.

        Returns:
            A template rendering the end of the game with the specified winner message.
        """
        #del self.game_sessions[game_id]
        return template('end_game', message=winner, username=username)

    def user_history(self):
        username = request.forms.get('username')
        user_games = self.user_data.get_user_history(username)
        return template('user_history_page', username=username, user_games=user_games)

if __name__ == "__main__":
    app = GameAPI()
    app.run(host=host, port=serverPort, debug=True)