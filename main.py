import os, random, time, assets

f = open('word.txt', 'r')
word = random.choice(f.readlines()).strip().upper()
reveal = list(len(word)*'_')
lives = 7
game_won = False

print('Welcome to HANGMAN!')
time.sleep(1)
print('Game is starting..')
time.sleep(2)


def letter_check(letter, word):
    """
    Function to check if single letter is in word, if so replaces blank with letter.
    :param letter:
    :param word:
    :return:
    """
    global reveal
    global game_won
    global lives
    for i in range(0, len(word)):
        letter = word[i]
        if guess == letter:
            reveal[i] = guess
    if '_' not in reveal:
        game_won = True
    else:
        game_won = False


def status():
    """
    Current status of lives remaining, changes assets picture.
    :return:
    """
    os.system('cls')
    print(assets.pictures[7-lives])
    print(' '.join([str(e) for e in reveal]))
    print('You have', lives, 'lives remaining!')


while game_won == False and lives > 0:
    status()
    guess = input('Guess a letter or word: ')
    guess = guess.upper()
    if guess == word:
        game_won = True
    if len(guess) == 1 and guess in word:
        letter_check(guess, word)
    else:
        lives -= 1


if game_won:
    print('Well done you won! The final word was', word)
else:
    print('You failed! The word was', word)

