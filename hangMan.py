print("This is a game of hangman. Your goal is to figure out the word by \nguessing the letters of that word. You have 10 guesses.")
i=0
word=("potato")
letters=set()
while i < 10:
    guess=input("Please guess a letter: ")
    if guess in word:
        letters.add(guess)
        if all(letter in letters for letter in word):
            print("Nice job! The word is potato!")
    i+=1   
if i == 10:
    print("You ran out of guesses. Try again!")