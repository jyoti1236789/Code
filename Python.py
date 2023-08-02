import random

def get_user_choice():
    user_choice = input("Enter your choice (Rock/Paper/Scissors): ").strip().lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Please enter Rock, Paper, or Scissors: ").strip().lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "Congratulations! You win!"
    else:
        return "Sorry, you lose. Better luck next time!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()
  
