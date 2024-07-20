import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    while True:
        # User input
        user_choice = input("\nChoose rock, paper, or scissors (or 'q' to quit): ").lower()

        if user_choice == 'q':
            print("\nThanks for playing!")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        # Computer randomly chooses
        computer_choice = random.choice(choices)
        
        # Display choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        # Display scores
        print(f"\nYour score: {user_score}")
        print(f"Computer's score: {computer_score}")
    
    # End of game
    print("\nFinal Scores:")
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")

# Start the game
rock_paper_scissors()