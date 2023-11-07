import random
def get_number():
    return random.randint(1, 100)
def get_guess():
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Number Guessing Game! We will play three games together.")

    total_guesses = 0

    for x in range(3):
        target_number = get_number()
        print("Game:",(x + 1), "I'm thinking of a number between 1 and 100.")

        guesses = 0

        while True:
            player_guess = get_guess()
            guesses += 1

            if player_guess < target_number:
                print("Too low. Try a higher number.")
            elif player_guess > target_number:
                print("Too high. Try a lower number.")
            elif player_guess == target_number:
                print("Congratulations! You guessed the number", target_number, "in", guesses, "tries.")
                total_guesses += guesses
                break

    average_guesses = total_guesses / 3
    print("Average number of guesses over 3 games: ", average_guesses)

main()
