import random

f = open('word.txt', 'r')

word = 'HAPPINESS'
reveal = list(len(word)*'_')
lives = 7
gameWon = False


while gameWon == False and lives > 0:
    print(reveal)
    guess = input('Guess a letter or word: ')
    guess = guess.upper()

    if guess == word:
        gameWon = True
    if len(guess) == 1 and guess in word:
        for i in range(0,len(word)):
            letter = word[i]
            if guess == letter:
                reveal[i] = guess
        if '_' not in reveal:
            gameWon = True
    else:
        lives -= 1


if gameWon:
    print('Well done you won!')
else:
    print('You failed! The word was', word)