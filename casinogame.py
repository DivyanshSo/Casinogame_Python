import random

def casino_game():
    print("Welcome to the Casino!")
    balance = 1000  # Initial balance for the player
    print(f"Your starting balance is: ${balance}")

    while balance > 0:
        print("\n1. Play the game")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == "2":
            print(f"Thanks for playing! You are leaving with ${balance}.")
            break
        elif choice == "1":
            try:
                bet = int(input("Enter your bet amount: "))
                if bet > balance or bet <= 0:
                    print("Invalid bet amount. Try again.")
                    continue

                print("Guess a number between 1 and 10:")
                guess = int(input("Your guess: "))
                if guess < 1 or guess > 10:
                    print("Invalid guess. Please pick a number between 1 and 10.")
                    continue

                winning_number = random.randint(1, 10)
                print(f"The winning number is: {winning_number}")

                if guess == winning_number:
                    print(f"Congratulations! You win ${bet * 2}.")
                    balance += bet
                else:
                    print("You lost this round. Better luck next time!")
                    balance -= bet

                print(f"Your current balance is: ${balance}")

            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid choice. Please select 1 or 2.")

    if balance == 0:
        print("You are out of money. Game over!")

#game will start...
casino_game()