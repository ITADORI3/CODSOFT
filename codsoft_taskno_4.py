import random
from enum import Enum

class Choice(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_input not in [choice.value for choice in Choice]:
        print("Invalid input. Please try again.")
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_input

def get_computer_choice():
    return random.choice([choice.value for choice in Choice])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == Choice.ROCK.value and computer == Choice.SCISSORS.value) or \
         (user == Choice.SCISSORS.value and computer == Choice.PAPER.value) or \
         (user == Choice.PAPER.value and computer == Choice.ROCK.value):
        return "user"
    else:
        return "computer"

def display_results(user, computer, winner):
    print(f"\nYour choice: {user}")
    print(f"Computer's choice: {computer}")

    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

def main():
    user_score = 0
    computer_score = 0
    total_rounds = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        display_results(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        total_rounds += 1
        print(f"\nYour score: {user_score}\nComputer score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        if play_again != "yes":
            break

    print(f"\nGame Over! Total rounds played: {total_rounds}")

if __name__ == "__main__":
    main()
