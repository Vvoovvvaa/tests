import random
import requests

def fetch_random_words(count=10):
    try:
        response = requests.get(f"https://random-word-api.herokuapp.com/word?number={count}")
        if response.status_code == 200:
            return response.json()
    except Exception:
        pass
    return ["python", "hangman", "programming", "developer", "algorithm"]

def get_picture(mistakes):
    stages = [
        """ 
         ------
         |    |
              |
              |
              |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
              |
              |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
         |    |
              |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
        /|    |
              |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
              |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
        /     |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
        / \\   |
              |
              |
        =========
        """
    ]
    print(stages[mistakes])

def hangman():
    words = fetch_random_words()
    word = random.choice(words)
    guessed = []
    mistakes = 0
    max_mistakes = 6

    print("Welcome to Hangman!")
    while mistakes < max_mistakes:
        get_picture(mistakes)
        print("\nWord:", ''.join([letter if letter in guessed else '_' for letter in word]))
        guess = input("Enter a letter: ").lower()
        if guess in guessed:
            print(f"You've already guessed '{guess}'.")
            continue
        guessed.append(guess)
        if guess in word:
            print(f"Correct! '{guess}' is in the word.")
        else:
            mistakes += 1
            print(f"Incorrect! '{guess}' is not in the word.")
        if all(letter in guessed for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    if mistakes == max_mistakes:
        get_picture(mistakes)
        print(f"\nYou lose! The word was: {word}")

def main():
    hangman()
    while input("Play again? (y/n): ").lower() == 'y':
        hangman()

if __name__ == "__main__":
    main()
