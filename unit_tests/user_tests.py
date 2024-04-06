from unittest import TestCase
from modules.user import user

class TestUser(TestCase):

    def setup(self):
        self.GameUser = user()

    def test_player_registration_success(self):
        result = self.GameUSer.register_player("test_user", "test_password")
        self.assertTrue(result, "Registration Successfull.")

    def test_player_login_success(self):
        self.GameUser.register_player("test_user", "test_password")
        result = self.GameUser.login_player("test_user", "test_password")
        self.assertTrue(result, "session_token", "Login will return a session token.")

    def test_player_profile_update_success(self):
        self.GameUser.register_player("test_player", "test_password")
        result = self.GameUser.update_profile("test_user", {"age": 20, "Location": "Country"})
        self.assertTrue(result, "Profile update is successful")

    def test_player_pass_change_success(self):
        self.GameUser.register_player("test_player", "test_password")
        result = self.GameUser.change_password("test_user", "new_password")
        self.assertTrue(result, "Password Change is Successfull.")

    def test_player_history_success(self):
        self.GameUser.register_player("test_user", "test_password")
        result = self.GameUser.get_user_history("test_user")
        expected_history = [{"activity": "played_game", "timestamp": "2024-02-17"}]
        self.assertEqual(result, expected_history, "User_inter history should match expected data.")
