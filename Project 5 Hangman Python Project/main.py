import random

def choose_word():
    words = ["python", "hangman", "developer", "programming", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("🎩 Welcome to Hangman! 💀")
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter! Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print("✅ Correct guess!")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! {attempts} attempts left.")
        
        if set(word) == guessed_letters:
            print("\n🎉 Congratulations! You guessed the word:", word)
            return

    print("\n💀 Game Over! The word was:", word)

hangman()