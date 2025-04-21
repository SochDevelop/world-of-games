import CurrencyRouletteGame
import GuessGame
import MemoryGame
import Score

difficulty = 0

def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play."


def load_game():
    global difficulty
    game_number = int(input("Please choose a game to play:\n"
                            "1. Memory Game a sequence of numbers will appear for 1 second and you have to"
                            "guess it back\n"
                            "2. Guess Game - guess a number and see if you chose like the computer\n"
                            "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))

    difficulty = int(input("Please choose game difficulty from 1 to 5: "))

    if game_number > 3 or game_number < 1:
        print("input suppose to be a number between 1 to 3")
        return
    if difficulty > 5 or difficulty < 1:
        print("difficulty suppose to be a number between 1 to 5.")
        return
    if game_number == 1:
        if MemoryGame.play(difficulty):
            Score.add_score(difficulty)
    elif game_number == 2:
        if GuessGame.play(difficulty):
            Score.add_score(difficulty)
    elif game_number == 3:
        if CurrencyRouletteGame.play(difficulty):
            Score.add_score(difficulty)
