import random

from pokemons.pokemon import Pokemon

import random

from pokemons.pokemon import Pokemon
from utils import Logger
from utils.formatter import Formatter


class ElectricPokemon(Pokemon):
    """Electric Pokemon, known for their ability to paralyze opponents and charge up for a powerful attack.

    Attributes:
        charge (bool): Indicates if the next attack is charged for extra damage.
    """

    def __init__(self, name, level):
        super().__init__(name, level, 'Electric')
        self.charge = False  # Initially not charged

    def attack(self, other):
        """Performs an electric attack which may paralyze the opponent or charge up for a powerful next attack."""
        outcome = random.random()  # Generates a single random outcome for multiple uses
        if self.charge:
            enhanced_damage = self.attack_power * 1.5
            Logger.log_info(f"{self.name} releases a charged attack dealing {Formatter.format_damage(enhanced_damage)} damage!")
            other.take_damage(enhanced_damage)
            self.charge = False  # Reset charge after use
        else:
            super().attack(other)

        if outcome < 0.2:  # 20% chance to paralyze
            Logger.log_info(f"{other.name} is paralyzed and will miss their next turn.")
            # Here, we may implement actual paralysis effect in the game logic
            #  when we have next **Unicorn gaming company ^_^

        if outcome < 0.15:  # 15% chance to charge up the next attack
            self.charge = True
            Logger.log_info(f"{self.name} is charging up for the next attack.")

    def display_status(self):
        """Displays current status, including whether the Pokemon is charged."""
        super().display_status()
        charge_status = "charged" if self.charge else "not charged"
        Logger.log_info(f"{self.name} is currently {charge_status}.")
