
import random
# 2 digit number guessing game
secret_number = str(random.randint(10,99))
print("Guess the number. It has 2 digits.")

remaining_try = 7

while remaining_try > 0:
    player_guess = input('Enter your guess: ')
    
    if player_guess == secret_number:
        print("Congratulations! You Win!")
        break
    else:
        bulls = 0
        cows = 0
        
        if player_guess[0] == secret_number[0]:
            bulls += 1
        else:
            if player_guess[0] == secret_number[1]:
                cows += 1
            
        if player_guess[1] == secret_number[1]:
            bulls += 1
        else:
            if player_guess[1] == secret_number[0]:
                cows += 1
            
        print('bulls =', bulls)
        print('cows =', cows)
        
        remaining_try -= 1
        
        if remaining_try < 1:
            print('Sorry, you lost the game')
            print('The secret number was:', secret_number)
            break






