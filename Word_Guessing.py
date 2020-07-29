import random

lives = 9
words = ['pizza', 'fairy', 'teeth', 'shirt', 'welder', 'world', 'otter',
         'home', 'afraid', 'scary', 'time', 'attempt', 'beautiful', 'bounty',
         'aligator', 'curve', 'cork', 'count', 'dragon', 'castle', 'maiden',
         'knight', 'horse', 'tournament', 'joust', 'king', 'queen', 'fool',
         'rooster', 'crowd', 'bakery', 'hall', 'list', 'chain', 'sword', 'fire',
         'rumble', 'tremble', 'court', 'flower', 'visitor', 'guest', 'symbol']

secret_word = random.choice(words)

clue = []

index = 0

while index < len(secret_word):
    clue.append('?')
    index += 1

heart_symbol = u'\u2764'

guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1
        
while lives > 0:
    print(clue)
    print('Lives left= ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect. You lose a life')
        lives -= 1

if guessed_word_correctly:
    print('You Won! The secret word was ' + secret_word)
else:
    print('You Lost The secret word was ' + secret_word)

