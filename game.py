import random

class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.target_word = ""
        self.guesses_left = 6
        self.guessed_letters = set()
        self.word_in_progress = []

    def choose_word(self):
        self.target_word = random.choice(self.word_list)
        self.word_in_progress = ["_"] * len(self.target_word)

    def display_word(self):
        return " ".join(self.word_in_progress)

    def make_guess(self, letter):
        if letter in self.guessed_letters:
            return "You already guessed that letter!"

        self.guessed_letters.add(letter)

        if letter in self.target_word:
            for i in range(len(self.target_word)):
                if self.target_word[i] == letter:
                    self.word_in_progress[i] = letter
            if "_" not in self.word_in_progress:
                return "Congratulations! You guessed the word: {}".format(self.target_word)
        else:
            self.guesses_left -= 1
            if self.guesses_left == 0:
                return "Sorry, you ran out of guesses. The word was: {}".format(self.target_word)

        return self.display_word() + f"\nLives left: {self.guesses_left}"

# Example usage:
word_list = ["python", "hangman", "coding", "challenge", "game"]

custom_hangman = HangmanGame(word_list)
custom_hangman.choose_word()

print("Welcome to Hangman!")
print("Word to guess:", custom_hangman.display_word())

while custom_hangman.guesses_left > 0 and "_" in custom_hangman.word_in_progress:
    guess = input("Enter your guess: ").lower()
    result = custom_hangman.make_guess(guess)
    print(result)

print("Game over.")