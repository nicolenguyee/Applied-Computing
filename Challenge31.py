import random

# Step 1: Get the player's name
player_name = input("What is your name? ")
print(f"Hello, {player_name}! Let's play Rock, Paper, Scissors.")

# Step 2: Ask how many rounds (between 3 and 10), and validate input
while True:
    try:
        rounds = int(input("How many rounds would you like to play? (3 to 10): "))
        if 3 <= rounds <= 10:
            break  # Valid input, exit loop
        else:
            print("Please enter a number between 3 and 10.")
    except ValueError:
        print("That’s not a valid number. Please enter an integer between 3 and 10.")

# Initialize score counters
player_score = 0
computer_score = 0

# Step 3: Play the rounds
choices = ["rock", "paper", "scissors"]

for round_number in range(1, rounds + 1):
    print(f"\n--- Round {round_number} ---")
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    
    if player_choice not in choices:
        print("Invalid choice. You lose this round.")
        computer_score += 1
        continue  # Skip to next round

    computer_choice = random.choice(choices)
    print(f"The computer chose {computer_choice}.")

    # Step 4: Decide the winner of this round
    if player_choice == computer_choice:
        print("It's a draw!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or
        (player_choice == "paper" and computer_choice == "rock")
    ):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

# Step 5: Final results
print("\n--- Game Over ---")
print(f"{player_name}'s score: {player_score}")
print(f"Computer's score: {computer_score}")

if player_score > computer_score:
    print("Congratulations, you won the game!")
elif player_score < computer_score:
    print("The computer won the game. Better luck next time!")
else:
    print("It's a draw overall!")