from typing import List
from modules import store


class User:
    """Manages player registration, login, and other User_inter-related functionalities."""

    def __init__(self):
        """Initialize the UserModule."""
        # Stub implementation: Initialize internal data structure for User_inter data
        self.user_data = {}

    def register_player(self, username: str, password: str) -> bool:
        """Register a new player with the given username and password.

        Args:
            username (str): The username of the new player.
            password (str): The password of the new player.

        Returns:
            bool: True if registration is successful, False otherwise.
        """
        # Checking if username is not already taken
        if username in self.user_data:
            return False

        # Add new player to the data if registered
        self.user_data[username] = {"password": password, "history": []}
        store.save_user(self.user_data)
        return True

    def login_player(self, username: str, password: str) -> str:
        """Log in a player with the provided username and password.

        Args:
            username (str): The username of the player.
            password: (str): The password of the player.

        return:
            str: Session token for authenticated access.
        """
        # Checking id username provided and password matches
        user = store.load_user(username)
        self.user_data = user
        if username in self.user_data and self.user_data[username]["password"] == password:
            session_token = f"token_{username}"
            return session_token
        else:
            return ""

    def update_profile(self, username: str, new_data: dict) -> bool:
        """Update the profile of the player.

        Args:
            username (str): The username of the player.
            new_data (dict): New data to update in the player's profile.

        Returns:
            bool: True if profile update is successful, False otherwise.
        """
        # Checking if provided username exists
        if username in self.user_data:
            # Update User_inter's profile
            self.user_data[username].update(new_data)
            return True
        else:
            return False

    def change_password(self, username: str, new_password: str) -> bool:
        """Change the password of the player.

        Args:
            username (str): The username of the player.
            new_password (str): The new password for the player.

        Returns:
            bool: True if password change is successful, False otherwise.
        """
        # Checking if username provided exists
        if username in self.user_data:
            # Update the players password
            self.user_data[username]["password"] = new_password
            return True
        else:
            return False

    def get_user_history(self, username: str) -> List[dict]:
        """Retrieve the activity history of the player.

        Args:
            username (str): The username of the player.

        Returns:
            List[dict]: List of dictionaries representing the player's activity history.
        """
        # Checking is username exists
        if username in self.user_data:
            # Return players activity
            return self.user_data[username]["history"]
        else:
            return []