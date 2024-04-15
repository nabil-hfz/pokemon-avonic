import random
from battle.battle import Battle
from pokemons.types.air_pokemon import AirPokemon
from pokemons.types.earth_pokemon import EarthPokemon
from pokemons.types.electric_pokemon import ElectricPokemon
from pokemons.types.fire_pokemon import FirePokemon
from pokemons.types.water_pokemon import WaterPokemon
from utils import Logger, Formatter


class Game:
    """Main class to handle game operations like choosing Pokemon and battling."""

    def __init__(self):
        self.available_pokemons = [
            FirePokemon("Charizard", 10),
            AirPokemon("Pidgeotto", 8),
            WaterPokemon("Squirtle", 7),
            ElectricPokemon("Zapdos", 9),
            EarthPokemon("Golem", 8),
        ]
        self.current_pokemon = None
        self.battles_count = 0
        self.defeated_pokemons = []

    def main_menu(self):
        """Display the main menu and handle user interactions."""
        while True:
            Logger.log_info("Options")
            Logger.log_info("1. Pick Pokemon.")
            Logger.log_info("2. Start Battle.")
            Logger.log_info("3. Exit.")
            Logger.log_info("Your option: ")
            choice = input()
            if choice == '1':
                self.choose_pokemon()
            elif choice == '2':
                if self.current_pokemon:

                    self.initiate_battle()

                    self.display_pokemon_stats()

                    if self.game_is_over():
                        break
                else:
                    Logger.log_info("Please choose a Pokemon first.\n")
            elif choice == '3':
                Logger.log_info("Exiting game.")
                break
            else:
                Logger.log_info("Invalid option, try again.")
            print('\n')

    def choose_pokemon(self):
        """Lets the player choose their Pokemon from the available list."""
        if self.current_pokemon:
            Logger.log_info("You've already chosen a pokemon. Now you are switching it.")

        Logger.log_info("Available Pokemon:")
        for index, pokemon in enumerate(self.available_pokemons, start=1):
            Logger.log_info(
                f"{index}. {Formatter.format_name(pokemon.name)} (Level {pokemon.level}, Type: {pokemon.type})")

        while True:
            Logger.log_info("Pick your Pokemon by number: ")
            try:
                choice = int(input()) - 1
                if 0 <= choice < len(self.available_pokemons):

                    if self.current_pokemon:
                        self.mark_pokemon_as_unused(self.current_pokemon)

                    self.current_pokemon = self.available_pokemons[choice]
                    self.mark_pokemon_as_used(self.current_pokemon)
                    Logger.log_info(f"You have chosen {Formatter.format_name(self.current_pokemon.name)}.")
                    break
                else:
                    Logger.log_info("Invalid choice, please pick again.")
            except ValueError:
                Logger.log_error("Please enter a valid number.")

    def initiate_battle(self):
        """Starts a battle sequence with an opponent."""

        while True:
            Logger.log_info("Do you want to choose your opponent? (Yes/No)")
            response = input().strip().lower()
            if response == 'yes':
                opponent = self.choose_opponent()
                break
            elif response == 'no':
                opponents = [p for p in self.available_pokemons if
                             p != self.current_pokemon and p not in self.defeated_pokemons]
                opponent = random.choice(opponents)
                Logger.log_info(f"Your randomly selected opponent is {Formatter.format_name(opponent.name)}.")
                break
            else:
                Logger.log_info("Invalid response, please answer 'Yes' or 'No'.")

        Logger.log_info(f"Starting battle with {Formatter.format_name(opponent.name)}.")
        battle = Battle(self.current_pokemon, opponent)
        battle.start_fight()
        self.battles_count += 1

        if opponent.is_knocked_out():
            self.mark_pokemon_as_defeated(opponent)

    def display_pokemon_stats(self):
        """Displays statistics for the current Pokemon."""
        Logger.log_info(f"Battle Count: {self.battles_count}, "
                        f"Current Pokemon: {Formatter.format_name(self.current_pokemon.name)}, "
                        f"Type: {self.current_pokemon.type}, "
                        f"Level: {self.current_pokemon.level}, "
                        f"Health: {Formatter.format_health(self.current_pokemon.health)}/{Formatter.format_health(self.current_pokemon.max_health)}, "
                        f"Evasion: {self.current_pokemon.evasion}%")

    def choose_opponent(self):
        """Allows the player to manually select an opponent from the available list."""
        Logger.log_info("Choose your opponent:")
        valid_opponents = [p for p in self.available_pokemons if
                           p != self.current_pokemon and p not in self.defeated_pokemons]
        if not valid_opponents:
            Logger.log_info("No available opponents to choose from.")
            return None
        for index, pokemon in enumerate(valid_opponents, start=1):
            Logger.log_info(
                f"{index}. {Formatter.format_name(pokemon.name)} (Level {pokemon.level}, Type: {pokemon.type})")

        while True:
            Logger.log_info("Pick your opponent by number: ")
            try:
                choice = int(input()) - 1
                if 0 <= choice < len(valid_opponents):
                    return valid_opponents[choice]
                else:
                    Logger.log_info("Invalid choice, please pick again.")
            except ValueError:
                Logger.log_error("Please enter a valid number.")

    def mark_pokemon_as_defeated(self, pokemon):
        self.defeated_pokemons.append(pokemon)
        self.available_pokemons.remove(pokemon)

    def mark_pokemon_as_used(self, pokemon):
        self.available_pokemons.remove(pokemon)

    def mark_pokemon_as_unused(self, pokemon):
        self.available_pokemons.append(pokemon)

    def has_lost(self):
        if self.current_pokemon.is_knocked_out():
            Logger.log_info(
                f"{Formatter.format_name(self.current_pokemon.name)}(YOU) has been knocked out.")
            return True
        return False

    def finishes_all_opponents(self):
        if not self.available_pokemons:
            Logger.log_info("Congratulations, you are the ultimate champion!")
            return True
        return False

    def game_is_over(self):
        return self.has_lost() or self.finishes_all_opponents()
