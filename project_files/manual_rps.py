#%%
import random

def get_computer_choice() -> str:
    """Randomly chooses one of three options:
    0: Rock
    1: Paper
    2: Scissors

    Returns:
        str: Random choice of "rock", "paper", or "scissors".
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice() -> str:
    """Returns user choice of "rock", "paper", or "scissors".

    Returns:
        str: Returns user choice of "rock", "paper", or "scissors".
    """
    choice = input("Enter rock, paper, or scissors. ")
    
    if choice not in ["rock", "paper", "scissors", "Rock", "Paper", "Scissors"]:
        return
    else:
        choice = choice.lower()
        return choice

def get_winner(computer_choice, user_choice):
    """Compares output of get_computer_choice and get_user_choice functions
    and returns a statement of the result of the game according to the rules
    of rock-paper-scissors.

    Args:
        computer_choice (str): computer's choice of rock, paper, or scissors.
        user_choice (str): user's choice of rock, paper, or scissors.
    """
    if computer_choice == user_choice:
        print('It is a tie!')
    elif (
        (computer_choice == 'rock' and user_choice == 'scissors') or
        (computer_choice == 'paper' and user_choice == 'rock') or
        computer_choice == 'scissors' and user_choice == 'paper'
        ):
        print('You lost!')
    else:
        print('You won!')

def play():
    """Plays the game of rock-paper-scissors.
    """
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    if user_choice in ["rock", "paper", "scissors"]:
        get_winner(computer_choice, user_choice)
    else:
        print('Invalid input')


