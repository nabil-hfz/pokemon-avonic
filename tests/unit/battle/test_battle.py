import unittest
from unittest.mock import MagicMock

from battle.battle import Battle


class TestBattle(unittest.TestCase):

    def setUp(self):
        # Create mock Pokemon objects
        self.pokemon1 = MagicMock()
        self.pokemon2 = MagicMock()

        # Set names for clarity in output
        self.pokemon1.name = "Pikachu"
        self.pokemon2.name = "Charmander"

        # Initialize the Battle with these mock Pokemon
        self.battle = Battle(self.pokemon1, self.pokemon2)

    def test_initialization(self):
        """Test that the Battle initializes with two Pokemon."""
        self.assertEqual(self.battle.pokemon1, self.pokemon1)
        self.assertEqual(self.battle.pokemon2, self.pokemon2)
        self.assertEqual(self.battle.turn, 1)

    def test_turn_swapping(self):
        """Test that turns are swapped correctly."""
        self.battle.swap_turn()
        self.assertEqual(self.battle.turn, 2)
        self.battle.swap_turn()
        self.assertEqual(self.battle.turn, 1)

    def test_take_turn(self):
        """Test that a turn proceeds correctly."""
        self.pokemon2.is_knocked_out.return_value = False
        self.battle.take_turn()

        # Check if the right methods were called
        self.pokemon1.attack.assert_called_once_with(self.pokemon2)
        self.pokemon2.display_status.assert_called_once()

        # Verify turn swapping logic when no Pokemon is knocked out
        self.assertEqual(self.battle.turn, 2)

    def test_victory_condition(self):
        """Test that the battle ends when one Pokemon is knocked out."""
        self.pokemon2.is_knocked_out.return_value = True
        self.pokemon1.is_knocked_out.return_value = False

        # Start the fight and check for the correct winner
        with self.assertLogs(level='INFO') as log:
            self.battle.start_fight()
            self.assertIn("Pikachu wins the battle!", log.output[0])
