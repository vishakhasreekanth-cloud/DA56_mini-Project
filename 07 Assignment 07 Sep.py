import random

# PART 1: While Loop & Control Statements
# Number Guessing Game

print("--- Part 1: Number Guessing Game ---")

# 1. Set Up the Game
secret_number = random.randint(1, 10)
attempts = 3

# 2. Implement the Guessing Logic using a while loop
while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))

    # Check if guess is out of range
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue  # Skip reducing attempt count / rest of loop for invalid input

    # Decrement attempt counter for valid guesses
    attempts -= 1

    # Check the guess against the secret number
    if guess > secret_number:
        print("Too high. Try again.")
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break  # Exit loop immediately when correct
else:
    # Executes only if the while loop finishes without hitting a 'break'
    print("Better luck next time!")

print("\n" + "=" * 40 + "\n")

# PART 2: For Loop
# Multiplication Table Generator

print("--- Part 2: Multiplication Table Generator ---")

num = int(
    input("Enter the number for which you want the multiplication table: ")
)

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")

print("\n" + "=" * 40 + "\n")


# PART 3: Function
# BMI Calculator

print("--- Part 3: BMI Calculator ---")


# 1. Define the calculate_bmi function
def calculate_bmi(weight, height):
    return weight / (height**2)


# 2. Prompt the user for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# 3. Calculate and display the BMI
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")