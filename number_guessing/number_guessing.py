import random

number =  random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Guess the number (1 to 100)")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempts {attempts+1}: Enter the your guess:"))
        attempts += 1

        if guess == number:
            print("correct ! you guessing it .")
            break
        elif guess < number:
            print('Too low!')

        else:
            print("Too high!")
    
    except ValueError:
        print('please enter invalid number.')

if attempts == max_attempts and guess != number:
    print(f"out of attempts! The number was {number }.")