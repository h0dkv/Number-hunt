import random

def choose_difficulty():
    print("\nChoose a difficulty:")
    print("1️⃣ Easy (1–20, 6 attempts)")
    print("2️⃣ Medium (1–50, 7 attempts)")
    print("3️⃣ Hard (1–100, 8 attempts)")

    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            return 20, 6
        elif choice == "2":
            return 50, 7
        elif choice == "3":
            return 100, 8
        else:
            print("❌ Invalid choice. Try again.")

def play_game():
    max_number, max_attempts = choose_difficulty()
    secret_number = random.randint(1, max_number)

    print(f"\n🎯 I'm thinking of a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    attempts = 0

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}: ")

        if not guess.isdigit():
            print("❌ Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("📉 Too low!")
        elif guess > secret_number:
            print("📈 Too high!")
        else:
            print(f"\n🎉 YOU WIN! You guessed the number in {attempts} attempts.")
            return

    print(f"\n💀 Game Over! The number was {secret_number}.")

def main():
    print("🎮 Welcome to NUMBER HUNT 🎮")

    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("\n👋 Thanks for playing Number Hunt!")
            break

if __name__ == "__main__":
    main()
