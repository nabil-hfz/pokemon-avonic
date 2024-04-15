import random

from pokemons.pokemon import Pokemon
from utils import Logger
from utils.formatter import Formatter


class EarthPokemon(Pokemon):
    """Earth Pokemon, known for high defense and the ability to regenerate health.

    Increases defense upon initialization and has a chance to cause significant disruption
    in battle with an earthquake effect that makes the opponent miss a turn.
    """

    def __init__(self, name, level):
        super().__init__(name, level, 'Earth')
        self.defense *= 1.2  # Increase defense by 20%
        self.regen_rate = 0.05  # Set regeneration rate to 5% of max health

    def attack(self, other):
        """Attacks another Pokemon and potentially cause them to miss their next turn due to an earthquake."""
        super().attack(other)
        if random.random() < 0.1:  # 10% chance to cause earthquake
            Logger.log_info(f"{Formatter.format_name(other.name)} is disoriented by an earthquake and misses next turn!")

        self.regenerate_health()

    def regenerate_health(self):
        """Regenerates health after each attack, up to the maximum health."""
        if self.health < self.max_health:
            heal = self.max_health * self.regen_rate
            actual_heal = min(heal, self.max_health - self.health)  # Ensure not to exceed max health
            self.health += actual_heal
            Logger.log_info(f"{Formatter.format_name(self.name)} regenerates {Formatter.format_health(actual_heal)} health, total health now {Formatter.format_health(self.health)}")
