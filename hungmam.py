import random
import requests

def fetch_random_words(count=10):
    try:
        response = requests.get(f"https://random-word-api.herokuapp.com/word?number={count}")
        if response.status_code == 200:
            return response.json()
        else:
            print("Error 404")
    except Exception as e:
        print(f"Error: {e}. Using default list.")
        return ["python", "hangman", "programming", "developer", "algorithm"]

def barer(words):
    return random.choice(words)

def logik_words(word, guessed):
    return ''.join([letter if letter in guessed else '_' for letter in word])

def get_picture(mistakes):
    stages = [
        ''' 
         ------
         |    |
              |
              |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
              |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
         |    |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|    |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|\\   |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|\\   |
        /     |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|\\   |
        / \\   |
              |
              |
        =========
        '''
    ]
    print(stages[mistakes])

def hangman(name, words):
    word = barer(words)
    guessed = []
    mistakes = 0
    max_mistakes = 6

    print(f"Welcome to the Hangman game, {name}!")

    while mistakes < max_mistakes:
        get_picture(mistakes)
        print(f"\nWord: {logik_words(word, guessed)}")
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue

        guessed.append(guess)

        if guess in word:
            print(f"Correct! '{guess}' is in the word.")
        else:
            mistakes += 1
            print(f"Incorrect! '{guess}' is not in the word.")

        if logik_words(word, guessed) == word:
            print(f"\nCongratulations! You guessed the word: {word}")
            break

    if mistakes == max_mistakes:
        get_picture(mistakes)
        print(f"\nYou lose! The word was: {word}")

def main():
    name = input("Enter your name: ")
    if name == "marsel":
        print("Brooo,you dont lose)))")
        exit()
    words = fetch_random_words()

    while True:
        hangman(name, words)
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print(f"Thanks for playing, {name}! Goodbye.")
            break

if __name__ == "__main__":
    main()