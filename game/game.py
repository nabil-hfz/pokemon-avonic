import random
from battle.battle import Battle
from pokemons.types.air_pokemon import AirPokemon
from pokemons.types.earth_pokemon import EarthPokemon
from pokemons.types.electric_pokemon import ElectricPokemon
from pokemons.types.fire_pokemon import FirePokemon
from pokemons.types.water_pokemon import WaterPokemon
from utils import Logger


class Game:
    """Main class to handle game operations like choosing Pokemon and battling."""

    def __init__(self):
        self.available_pokemons = [
            FirePokemon("Charizard", 10),
            AirPokemon("Pidgeotto", 8),
            WaterPokemon("Squirtle", 7),
            ElectricPokemon("Zapdos", 9),
            EarthPokemon("Golem", 8)
        ]
        self.current_pokemon = None
        self.battles_count = 0

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
                    if not self.current_pokemon.is_knocked_out():
                        self.display_pokemon_stats()
                    else:
                        Logger.log_info(f"{self.current_pokemon.name} has been knocked out.")
                        break
                else:
                    Logger.log_info("Please choose a Pokemon first.")
            elif choice == '3':
                Logger.log_info("Exiting game.")
                break
            else:
                Logger.log_info("Invalid option, try again.")
            print('\n')

    def display_pokemon_stats(self):
        """Displays statistics for the current Pokemon."""
        Logger.log_info(f"Battle Count: {self.battles_count}, "
                        f"Current Pokemon: {self.current_pokemon.name}, "
                        f"Type: {self.current_pokemon.type}, "
                        f"Level: {self.current_pokemon.level}, "
                        f"Health: {self.current_pokemon.health}/{self.current_pokemon.max_health}, "
                        f"Evasion: {self.current_pokemon.evasion}%")

    def choose_pokemon(self):
        """Lets the player choose their Pokemon from the available list."""
        Logger.log_info("Available Pokemon:")
        for index, pokemon in enumerate(self.available_pokemons, start=1):
            Logger.log_info(f"{index}. {pokemon.name} (Level {pokemon.level}, Type: {pokemon.type})")

        while True:
            Logger.log_info("Pick your Pokemon by number: ")
            choice = int(input())
            if 0 <= choice - 1 < len(self.available_pokemons):
                self.current_pokemon = self.available_pokemons[choice - 1]
                Logger.log_info(f"You have chosen {self.current_pokemon.name}.")
                break
            else:
                Logger.log_info("Invalid choice, please pick again.")

    def initiate_battle(self):
        """Starts a battle sequence with an opponent."""
        while True:
            Logger.log_info("Do you want to choose your opponent? (Yes/No)")
            response = input().strip().lower()
            if response == 'yes':
                opponent = self.choose_opponent()
                break
            elif response == 'no':
                opponent = random.choice([p for p in self.available_pokemons if p != self.current_pokemon])
                Logger.log_info(f"Your randomly selected opponent is {opponent.name}.")
                break
            else:
                Logger.log_info("Invalid response, please answer 'Yes' or 'No'.")

        Logger.log_info(f"Starting battle with {opponent.name}.")
        battle = Battle(self.current_pokemon, opponent)
        battle.start_fight()
        self.battles_count += 1

    def choose_opponent(self):
        """Allows the player to manually select an opponent from the available list."""
        Logger.log_info("Choose your opponent:")
        valid_opponents = [p for p in self.available_pokemons if p != self.current_pokemon]
        for index, pokemon in enumerate(valid_opponents, start=1):
            Logger.log_info(f"{index}. {pokemon.name} (Level {pokemon.level}, Type: {pokemon.type})")

        while True:
            Logger.log_info("Pick your opponent by number: ")
            choice = int(input())
            if 0 <= choice - 1 < len(valid_opponents):
                return valid_opponents[choice - 1]
            else:
                Logger.log_info("Invalid choice, please pick again.")
