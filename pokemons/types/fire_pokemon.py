import random
from pokemons.pokemon import Pokemon
from enum import Enum

from utils import Logger, Formatter


class FirePokemonTypes(Enum):
    """Enum for different types of fire-based attacks, specifying their additional damage."""
    fire_blast = (4, "A powerful blast of fire.")
    flame_thrower = (6, "A continuous stream of flames.")


class FirePokemon(Pokemon):
    """Fire Pokemon class, capable of inflicting burn damage with special fire attacks."""

    def __init__(self, name, level, fire_type=FirePokemonTypes.fire_blast):
        super().__init__(name, level, 'Fire')
        self.fire_type = fire_type

    def attack(self, other):
        """Performs a fire-type attack that may cause additional burn damage."""
        super().attack(other)  # Use the base class attack logic
        if other.health > 0 and random.random() < 0.25:  # 25% chance to inflict burn damage
            burn_damage = self.fire_type.value[0]  # Accessing damage value from the enum
            Logger.log_info(
                f"{Formatter.format_name(self.name)} is burned! {self.fire_type.name} deals an extra {burn_damage} damage.")
            other.take_damage(burn_damage)  # Inflict additional burn damage

    def display_status(self):
        """Displays current status, including the type of fire attack."""
        super().display_status()
        Logger.log_info(
            f"{Formatter.format_name(self.name)} is ready to use {self.fire_type.name}, which {self.fire_type.value[1]}")
