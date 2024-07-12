import random

def generate_number(length):
    return str(random.randint(10**(length-1), 10**length - 1))

def get_hint(number, guess):
    hint = ""
    for i in range(len(number)):
        if number[i] == guess[i]:
            hint += "B"  # Black peg, correct digit in correct position
        elif guess[i] in number:
            hint += "W"  # White peg, correct digit in incorrect position
        else:
            hint += "-"  # No peg, incorrect digit
    return hint

def play_mastermind():
    player1_number = generate_number(4)  # Generate a 4-digit number
    print("Player 1 has set a 4-digit number. Player 2, start guessing!")

    attempts = 0
    while True:
        player2_guess = input("Enter your 4-digit guess: ")
        if len(player2_guess)!= 4 or not player2_guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue
        attempts += 1
        hint = get_hint(player1_number, player2_guess)
        print(f"Hint: {hint}")
        if hint == "BBBB":
            print(f"Congratulations, Player 2! You guessed the number in {attempts} attempts.")
            break

    # Now, Player 2 sets the number and Player 1 guesses
    player2_number = generate_number(4)
    print("Player 2 has set a new 4-digit number. Player 1, start guessing!")

    attempts = 0
    while True:
        player1_guess = input("Enter your 4-digit guess: ")
        if len(player1_guess)!= 4 or not player1_guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue
        attempts += 1
        hint = get_hint(player2_number, player1_guess)
        print(f"Hint: {hint}")
        if hint == "BBBB":
            print(f"Congratulations, Player 1! You guessed the number in {attempts} attempts.")
            if attempts < attempts:
                print("Player 1 wins the game and is crowned Mastermind!")
            else:
                print("Player 2 wins the game and is crowned Mastermind!")
            break

play_mastermind()
