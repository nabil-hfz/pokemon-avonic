import unittest
from unittest.mock import patch

from pokemons import Pokemon
from utils import Formatter


class TestPokemon(unittest.TestCase):

    def setUp(self):
        """Create a Pokemon instance to use in all tests."""
        self.pokemon = Pokemon("Bulbasaur", 5, "Grass")
        self.opponent = Pokemon("Charmander", 5, "Fire")

    def test_initialization(self):
        """Test Pokemon initialization."""
        self.assertEqual(self.pokemon.name, "Bulbasaur")
        self.assertEqual(self.pokemon.level, 5)
        self.assertEqual(self.pokemon.type, "Grass")
        self.assertEqual(self.pokemon.health, 50)
        self.assertEqual(self.pokemon.max_health, 50)
        self.assertEqual(self.pokemon.attack_power, 10)
        self.assertEqual(self.pokemon.defense, 7.5)
        self.assertEqual(self.pokemon.evasion, 0.0)

    def test_health_setter(self):
        """Test that the health setter does not allow negative values."""
        self.pokemon.health = -10
        self.assertEqual(self.pokemon.health, 0)

    @patch('random.random', return_value=0.1)  # Simulate an attack that hits (evasion fails)
    @patch('utils.Logger.log_info')
    def test_attack_hits(self, mock_log, mock_random):
        """Test successful attack."""
        self.opponent.defense = 5
        self.pokemon.attack(self.opponent)
        expected_damage = 5  # 10 attack - 5 defense
        mock_log.assert_called_with(
            f"{Formatter.format_name(self.opponent.name)} now has {Formatter.format_damage(self.opponent.max_health - expected_damage)} health.")
        self.assertEqual(self.opponent.health, 45)

    @patch('random.random', return_value=0.99)  # Simulate an attack that misses
    @patch('utils.Logger.log_info')
    def test_attack_misses(self, mock_log, mock_random):
        """Test an attack that misses due to high evasion."""
        self.opponent.evasion = 1.0  # Guaranteed evasion
        self.pokemon.attack(self.opponent)
        mock_log.assert_called_with(
            f"{self.pokemon.name}'s attack missed due to {self.opponent.name}'s evasion!")

    def test_take_damage(self):
        """Test taking damage and health reduction."""
        self.pokemon.take_damage(20)
        self.assertEqual(self.pokemon.health, 30)

    def test_is_knocked_out(self):
        """Test if Pokemon is correctly identified as knocked out."""
        self.pokemon.health = 0
        self.assertTrue(self.pokemon.is_knocked_out())

    @patch('utils.Logger.log_info')
    def test_display_status(self, mock_log):
        """Test display status logs correct information."""
        self.pokemon.display_status()
        mock_log.assert_called_once()
