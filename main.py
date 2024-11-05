import random
import time

# Variables
MOVES = ["rock", "paper", "scissors"]
score = {
    "wins": 0,
    "ties": 0,
    "losses": 0
}

# Function to get user move
def get_user_move():
    while True:
        answer = input("Enter your move (rock, paper, scissors, \"exit\" to quit): ").lower()
        if answer in MOVES:
            return answer
        elif answer == "exit":
            print("Thanks for playing!")
            print(f"Final score: Wins: {score['wins']} Ties: {score['ties']} Losses: {score['losses']}")
            quit()  # Exit the game
        else:
            print("Invalid input. Please enter a valid move (rock, paper, scissors, or \"exit\" to quit).\n")

# Play function
def play():
    user_move = get_user_move()
    computer_move = random.choice(MOVES)
    print(f"\nUser: {user_move}")
    print(f"Computer: {computer_move}")

    # Possible outcomes
    if user_move == computer_move:
        score["ties"] += 1
        print("It's a tie!\n")
    elif (user_move == "rock" and computer_move == "paper") or \
         (user_move == "paper" and computer_move == "scissors") or \
         (user_move == "scissors" and computer_move == "rock"):
        score["losses"] += 1
        print("You lose!\n")
    else:
        score["wins"] += 1
        print("You win!\n")

    # Show current score
    print(f"Wins: {score['wins']} Ties: {score['ties']} Losses: {score['losses']}\n")
    
    time.sleep(1)  # Pause for 1 second to improve UX before the next rounds

# Main function to start the game
def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        play()

if __name__ == "__main__":
    main()
