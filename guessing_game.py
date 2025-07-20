#!/usr/bin/env python3
"""
Number Guessing Game
A simple game where you try to guess a random number.
"""

import random

def guessing_game():
    """Main guessing game function."""
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return True
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
            
            # Give hints based on how close they are
            difference = abs(guess - secret_number)
            if difference <= 5:
                print("🔥 You're very close!")
            elif difference <= 15:
                print("🌡️ Getting warmer...")
            
        except ValueError:
            print("❌ Please enter a valid number!")
            attempts -= 1  # Don't count invalid inputs
    
    print(f"\n💀 Game over! The number was {secret_number}")
    return False

def main():
    """Main program loop."""
    while True:
        won = guessing_game()
        
        # Ask if they want to play again
        while True:
            play_again = input("\nWould you like to play again? (y/n): ").lower()
            if play_again in ['y', 'yes']:
                print("\n" + "="*40)
                break
            elif play_again in ['n', 'no']:
                print("Thanks for playing! 👋")
                return
            else:
                print("Please enter 'y' or 'n'")

if __name__ == "__main__":
    main()