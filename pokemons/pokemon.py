import random

from utils import Logger
from utils.formatter import Formatter


class Pokemon:
    """A base class for all Pokemon types, extended with special abilities.

      Attributes:
          name (str): The name of the Pokemon.
          level (int): The level of the Pokemon, affecting its stats.
          type (str): The type of the Pokemon, influencing battle interactions.
          health (int): Current health of the Pokemon. Cannot drop below zero.
          max_health (int): Maximum health of the Pokemon.
          attack_power (int): Base attack power of the Pokemon.
          defense (float): Defensive strength of the Pokemon.
          evasion (float): Base evasion set to 0 for all Pokemon.
      """

    def __init__(self, name, level, pokemon_type):
        self.name = name
        self.level = level
        self.type = pokemon_type
        self._health = self.max_health = level * 10
        self.attack_power = level * 2
        self.defense = level * 1.5
        self.evasion = 0.0

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        else:
            self._health = value

    def attack(self, other):
        """Attempts to perform an attack on another Pokemon, which may miss based on evasion."""
        if random.random() > other.evasion:
            damage = self.attack_power - other.defense
            damage = max(damage, 0)  # Prevent damage from being negative
            Logger.log_info(
                f"{Formatter.format_name(self.name)} attacks {Formatter.format_name(other.name)} causing {Formatter.format_damage(damage)} damage.")
            other.take_damage(damage)
        else:
            Logger.log_info(
                f"{Formatter.format_name(self.name)}'s attack missed due to {Formatter.format_name(other.name)}'s evasion!")

    def take_damage(self, amount):
        """Reduces health by the specified amount after an attack. Health cannot fall below zero."""
        self.health = max(self.health - amount, 0)
        Logger.log_info(
            f"{Formatter.format_name(self.name)} now has {Formatter.format_damage(self.health)} health.")

    def is_knocked_out(self):
        """Checks if the Pokemon's health is zero."""
        return self.health <= 0

    def display_status(self):
        """Shows current health, level, and evasion."""
        Logger.log_info(
            f"{Formatter.format_name(self.name)} (Type: {self.type}): Level {self.level}, Health {Formatter.format_health(self.health)}/{self.max_health}, Evasion: {self.evasion:.0%}")
