import random 
from words import word_list

def getRandom():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('lets Play Hangman! ')
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
      guess = input("Enter your guess : ").upper()
      if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
          print("You have already guessed the letter " , guess)
        elif guess not in word:
          print(guess , "is not in the word. ")
          tries -= 1
          guessed_letters.append(guess)
        else:
          print("Good job" , guess , "is in the word!")
          guessed_letters.append(guess)
          word_as_list = list(word_completion)
          indices = [i for i, letter in enumerate(word) if letter == guess ]
          for index in indices:
            word_as_list[index] = guess
            word_completion = "".join(word_as_list)
          if "_" not in word_completion:
            guessed = True
  
      elif len(guess) == 1 and guess.isalpha():
        if guess in guessed_words:
          print("You have already guessed the letter " , guess)
        elif guess != word:
          print(guess , "is not in the word. ")
          tries -= 1
          guessed_words.append(guess)
        else:
          guessed = True
          word_completion = word
      else:
        print("Not a valid guess")
        print(displayHangman(tries))
        print(word_completion)
      if guessed:
        print("Congrats! You guessed the word ! You win!")
      else:
        print("sorry , you ran out of tries . The word was " + word + "")

      print(word_completion)
     

def displayHangman(tries):
  if progress == 0:
    print("No hanged parts yet! :)")
	for i in range(0, progress):
		if i == 0:
			print(" O")
		elif i == 1 and progress == 2:
			print(" |")
		elif i == 2 and progress == 3:
			print("/|")
		elif i == 3 and progress >= 4:
			print("/|\\")
		elif i == 4 and progress == 5:
			print("/")
			print("Yikes.")
		elif i == 5 and progress == 6:
			print("/ \\")
       


def main():
    word = getRandom()
    print(word)
    play(word)

    while input('Do you want to play again(Y/N): ').upper() == 'Y':
      word = getRandom()
      play(word)

    if __name__ == "__main__":
      main()