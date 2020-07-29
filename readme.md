# <font color = teal>Simple Games in Python</font>
July 2020 

These are short scripts that will play simple word or number guessing games in Python. They were written to practice fundamental Python basics. Files are saved as Jupyter notebooks.

## <font color = teal>Cows_and_Bulls_2digit</font>
A random 2 digit number from 10 to 99 is generated, player attempts to guess the number by entering a 2 digit number. Feedback tells the player if either digit is the correct number in the correct place (bull) or if correct digit in wrong place (cow). Game ends when player guesses the number or runs out of guesses.
- Libraries needed: Random
- Python skills learned: importing from library, defining functions, loops, assigning variables, getting input from user

## <font color = teal>Cows_and_Bulls_4digit</font>
A random 4 digit number is generated by selecting a random integer 0-9 for each digit. The player attempts to guess the number by entering a 4 digit number. Feedback tells the player if any digit is the correct number in the correct place (bull) or if correct digit in wrong place (cow). Game ends when player guesses the number or runs out of guesses.
- Libraries needed: Random
- Python skills learned: running multiple functions, global variables, recursive functions
- Updates completed: added introduction instructions and play again feature

## <font color = teal>Word_Guessing_Game</font>
A random word is selected from a list of words. Player enters a letter and receives feedback if letter is in the word and the position of the letter in the word if present. If letter not in word player loses a life. Game ends when player reveals all letters in the word, types the completed word, or runs out of lives.
- Libraries needed: Random
- Python skills learned: more global variables, using unicode characters
- Updates needed: add introduction and play again, replace set word list with imported list of words