import random

# Fixed: All lowercase, no spaces, fixed 'hangman' spelling
words = ["python", "codealpha", "developer", "hangman", "program"]
choose_word = random.choice(words)
guessed_letter = []
attempt = 6

print("✨ Welcome to Hangman! ✨")

while attempt > 0:
    
    display_word = ""
    
    for letter in choose_word:
        if letter in guessed_letter:
            display_word += letter + " "
        else:
            display_word += "_ "  # Fixed: Added space to match the letter layout

    print("\nWord to guess: ", display_word)
    print(f"Attempts left: {attempt}")

    if "_ " not in display_word:  # Fixed: Match the space formatting
        print("🎉 Congratulations! You won!")
        break        

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single valid letter.")
        continue

    if guess in guessed_letter:
        print("⚠️ You already guessed that letter! Try a different one.")
        continue

    guessed_letter.append(guess)

    if guess in choose_word:
        print(f"✅ Good job! '{guess}' is in the word.")
    else:
        print(f"❌ Oops! '{guess}' is not in the word.")
        attempt -= 1  # Fixed: Changed from =- to -= to properly subtract

# Fixed: Moved this OUTSIDE the while loop so it triggers when attempts hit 0
if attempt == 0:
    print(f"\n💀 Game Over! You ran out of attempts. The word was: '{choose_word}'")