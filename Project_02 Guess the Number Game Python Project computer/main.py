import random

def computer_guess():
    low = 1
    high = 10
    feedback = ""

    print("Think of a number between 1 and 10, and I'll try to guess it! 🤔")

    while feedback != "c":
        guess = random.randint(low, high)
        print(f"My guess is: {guess}")

        feedback = input("Is it too high (h), too low (l), or correct (c)? ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay! I guessed your number {guess} correctly! 🎉")

computer_guess()