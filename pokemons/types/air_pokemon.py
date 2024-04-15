import random

from pokemons.pokemon import Pokemon
from utils import Logger, Formatter


class AirPokemon(Pokemon):
    """Air Pokemon, characterized by high agility, can push back opponents and boost evasion.

    Attributes:
        evasion (float): The chance to evade an attack, capped at a maximum value.
    """

    MAX_EVASION = 0.25  # Maximum evasion cap

    def __init__(self, name, level):
        super().__init__(name, level, 'Air')
        self.evasion = 0.1  # 10% base evasion chance

    def attack(self, other):
        """Performs an attack and potentially push back the opponent or increase evasion."""
        if super().attack(other):  # Ensure attack is processed only if it happens
            outcome = random.random()
            if outcome < 0.15:  # 15% chance to push back
                Logger.log_info(
                    f"{Formatter.format_name(self.name)} is pushed back and delays their attack.")

            if outcome < 0.1 and self.evasion < self.MAX_EVASION:
                self.evasion += 0.05
                self.evasion = min(self.evasion, self.MAX_EVASION)
                Logger.log_info(
                    f"{Formatter.format_name(self.name)}'s evasion increased to {self.evasion:.0%}.")
