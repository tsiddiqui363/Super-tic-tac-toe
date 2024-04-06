import json




def save_game(game):
    """Saves the game state to a JSON file."""
    game_data = {
        'gameID': game.gameID,
        'player1': game.player1,
        'player2': game.player2,
        'gameState': game.gameState,
        'history': game.history
    }
    with open(f'game_{game.gameID}.json', 'w') as file:
        json.dump(game_data, file)
    print(f"Game {game.gameID} saved.")


def load_game(game, gameID):
    """Loads the game state from a JSON file."""
    try:
        with open(f'game_{gameID}.json', 'r') as file:
            game_data = json.load(file)
            game.gameID = game_data['gameID']
            game.player1 = game_data['player1']
            game.player2 = game_data['player2']
            game.gameState = game_data['gameState']
            game.history = game_data['history']
            return True
    except FileNotFoundError:
        print(f"Game {gameID} not found.")
        return False


def save_user(user_dataq):
    """Saves the User_inter data to a JSON file."""

    with open(f'user_store.json', 'w') as file:
        json.dump(user_dataq, file)
    print(f"User_inter  saved.")


def load_user(username):
    """Loads the User_inter data from a JSON file."""
    try:
        with open(f'user_store.json', 'r') as file:
            user_data = json.load(file)
            return user_data
    except FileNotFoundError:
        print(f"User_store.json not found.")
        return None


