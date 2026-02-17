import numpy as np

# TODO [1]: implement the guessing_game function
def guessing_game(max: int, *, attempts: int) -> tuple[bool, tuple[int, ...], int]:
    """
    Docstring for guessing_game
    
    :param max: Description
    :type max: int
    :param attempts: Description
    :type attempts: int
    :return: Description
    :rtype: tuple[bool, tuple[int, ...], int]
    """
    chosen_int: int = np.random.randint(1, max + 1)
    guesses: list[int] = []
    print(f"Welcome to the Guessing Game, Guess a number between 1 and {max}. You have {attempts} attempts.")

    attempt = 1
    while attempt <= attempts:
        try:
            guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))
            guesses.append(guess)

            if guess < chosen_int:
                print("Too low!")
            elif guess > chosen_int:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the correct number: {chosen_int}.")
                return True, tuple(guesses), chosen_int

            attempt += 1

        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

    print(f"Sorry, you've run out of attempts. The correct number was {chosen_int}.")
    return False, tuple(guesses), chosen_int

# TODO [2]: implement the play_game function
def play_game()-> None:
    max_value:int = 20
    attempts:int = 5
    while True:
        player_won, guesses, chosen_int = guessing_game(max=max_value, attempts=attempts)
        if player_won:
            assert chosen_int in guesses, "Error: The chosen number is not in the guesses list."
            print("You won! Game over.")
            break
        else:
            assert chosen_int not in guesses ,"Error: The chosen number is in the guesses list."
            print("You lost! The correct number was not in your guesses.")
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != "yes":
                print("Thanks for playing! Goodbye.")
                break


