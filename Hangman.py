import random

from hangman import display_hangman
from answers import answers


def get_word() -> str:
    word = random.choice(answers)
    return word.upper()


WORD = get_word()


class Game:
    def __init__(self):
        self.word = WORD
        self.word_completion = "_" * len(self.word)
        self.guessed = False
        self.guessed_letters = []
        self.guessed_words = []
        self.tries = 6

    def start_game(self, guess):
        while not self.guessed and self.tries > 0:
            if len(guess) == 1 and guess.isalpha():
                if guess in self.guessed_letters:
                    print("You already guessed the letter", guess)
                elif guess not in self.word:
                    print(guess, "is not in the word.")
                    self.tries -= 1
                    self.guessed_letters.append(guess)
                else:
                    print("Good job,", guess, "is in the word!")
                    self.guessed_letters.append(guess)
                    word_as_list = list(self.word_completion)
                    indices = [i for i, letter in enumerate(self.word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        self.guessed = True
            elif len(guess) == len(self.word) and guess.isalpha():
                if guess in self.guessed_words:
                    print("You already guessed the word", guess)
                elif guess != self.word:
                    print(guess, "is not the word.")
                    self.tries -= 1
                    self.guessed_words.append(guess)
                else:
                    self.guessed = True
                    self.word_completion = self.word
            else:
                print("Not a valid guess.")
            print(display_hangman(self.tries))
            print(self.word_completion)
            print("\n")
        if self.guessed:
            print("Congrats, you guessed the word! You win!")
        else:
            print("Sorry, you ran out of tries. The word was " + self.word + ". Maybe next time!")


def main():
    game = Game()

    guess = input("Please guess a letter or word: ").upper()

    game.start_game(guess)

    while input("Play Again? (Y/N) ").upper() == "Y":
        Game()


if __name__ == '__main__':
    main()
