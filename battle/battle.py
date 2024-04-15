from utils import Logger, Formatter


class Battle:
    """Manages the interactions between two Pokemon in a fight."""

    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.turn = 1  # Start with pokemon1

    def start_fight(self):
        """Starts the fight and alternates turns until one is knocked out."""
        while not self.pokemon1.is_knocked_out() and not self.pokemon2.is_knocked_out():
            self.take_turn()

        winner = self.pokemon1 if self.pokemon2.is_knocked_out() else self.pokemon2
        Logger.log_info(f"{Formatter.format_name(winner.name)} wins the battle!\n")

    def take_turn(self):
        """Processes the current turn, then swaps."""
        attacker = self.pokemon1 if self.turn == 1 else self.pokemon2
        defender = self.pokemon2 if self.turn == 1 else self.pokemon1

        Logger.log_info(f"{Formatter.format_name(attacker.name)}'s turn to attack {defender.name}.")
        attacker.attack(defender)
        defender.display_status()

        if defender.is_knocked_out():
            return

        self.swap_turn()

    def swap_turn(self):
        """Swaps whose turn it is to attack."""
        self.turn = 2 if self.turn == 1 else 1
