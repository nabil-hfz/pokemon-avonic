import random

from pokemons.pokemon import Pokemon
from utils import Logger
from utils.formatter import Formatter


class WaterPokemon(Pokemon):
    """Water Pokemon, adept at hydrating to recover health and potentially dampening opponents' attacks."""

    def __init__(self, name, level):
        super().__init__(name, level, 'Water')

    def take_damage(self, amount):
        # Implements hydration to potentially recover health before taking damage
        if random.random() < 0.3:  # 30% chance to activate hydrate
            recovered_health = amount / 2
            self.health += recovered_health
            self.health = min(self.health, self.max_health)  # Ensure health does not exceed max
            Logger.log_info(
                f"{Formatter.format_name(self.name)} uses Hydrate to recover {Formatter.format_health(recovered_health)} health.")

        # Checks for dampening effect
        if random.random() < 0.2:  # 20% chance to dampen the incoming attack
            reduced_amount = amount * 0.1  # Reduce damage by 10%
            Logger.log_info(
                f"{Formatter.format_name(self.name)}'s splashing reduces the incoming damage by {reduced_amount}.")
            amount -= reduced_amount

        # Calls the superclass method to apply the damage
        super().take_damage(amount)

    def display_status(self):
        """Displays current health, level, and any active effects."""
        super().display_status()
        Logger.log_info(
            f"{Formatter.format_name(self.name)} has specialized water abilities that can mitigate damage and recover health.")
