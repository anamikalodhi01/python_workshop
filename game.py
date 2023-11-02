import random

def guess_number():
    return random.randint(1,100)  # random.randit is a method

target_number=guess_number()
attempts = 0

while True:
    user_guess = int(input("Guess the number: "))
    attempts+=1

    if user_guess == target_number:
        print("Congratulations! You guessed the number n" ,attempts, "attempts.")
        break
    elif user_guess < target_number:
        print("Try a higher number.")
    else:
        print("try a lower number.")