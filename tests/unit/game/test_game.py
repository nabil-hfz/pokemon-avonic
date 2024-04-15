import unittest
from unittest.mock import patch
from game.game import Game
from pokemons.types.air_pokemon import AirPokemon
from pokemons.types.fire_pokemon import FirePokemon


class TestGame(unittest.TestCase):

    def setUp(self):
        """Setup a game instance for each test."""
        self.game = Game()

    def test_initialization(self):
        """Test the initialization of the game."""
        self.assertIsInstance(self.game.available_pokemons[0], FirePokemon)
        self.assertEqual(len(self.game.available_pokemons), 5)

    @patch('builtins.input',
           side_effect=['1', '1', '3'])  # Choosing to pick a Pokemon, choosing the first one, then exiting
    @patch('utils.Logger.log_info')
    def test_main_menu_navigation(self, mock_log, mock_input):
        """Test main menu navigation."""
        with patch('game.game.Logger.log_info') as mocked_log:
            self.game.main_menu()
            mocked_log.assert_called_with("Exiting game.")

    @patch('builtins.input', side_effect=['1', '2', '2', '3'])
    def test_pokemon_choice_and_battle(self, mock_input):
        """Test choosing a Pokemon and initiating a battle."""
        with patch('game.game.Logger.log_info') as mocked_log, \
                patch.object(Game, 'initiate_battle', return_value=None) as mock_battle:
            self.game.main_menu()
            self.assertIsInstance(self.game.current_pokemon, AirPokemon)
            mock_battle.assert_called_once()

    @patch('builtins.input', side_effect=['1', '100', '1', '3'])  # Invalid choice then valid choice
    def test_invalid_pokemon_choice(self, mock_input):
        """Test handling of invalid Pokemon choice."""
        with patch('utils.Logger.log_info') as mocked_log:
            self.game.main_menu()
            mocked_log.assert_any_call("Invalid choice, please pick again.")
