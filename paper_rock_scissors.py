import random

def get_user_choice():
    while True:
        user_choice = input("Type Paper/Rock/Scissors or q to quit: ").lower()
        if user_choice == 'q':
            quit()
        elif user_choice in ["paper", "rock", "scissors"]:
            return user_choice
        else:
            print("Please type one of the options :(")

def determine_winner(computer_pick, user_choice):
    if computer_pick == user_choice:
        return "It's a Draw"
    elif (computer_pick == 'paper' and user_choice == 'rock') or \
         (computer_pick == 'scissors' and user_choice == 'paper') or \
         (computer_pick == 'rock' and user_choice == 'scissors'):
        return "Computer wins"
    else:
        return "User wins"

def main():
    print("Welcome to the paper-rock-scissors game!!")
    options = ["paper", "rock", "scissors"]
    computer_score = 0
    user_score = 0

    while user_score < 3 and computer_score < 3:
        user_choice = get_user_choice()
        computer_pick = random.choice(options)
        print("The computer chose:", computer_pick)
        result = determine_winner(computer_pick, user_choice)
        print(result)
        if result == "Computer wins":
            computer_score += 1
        elif result == "User wins":
            user_score += 1

    print('_' * 15)
    print("User score:", user_score)
    print("Computer score:", computer_score)

    if user_score == 3:
        print("Congratulations, you win the game!")
    else:
        print("Sorry, you lose the game.")

if __name__ == "__main__":
    main()
