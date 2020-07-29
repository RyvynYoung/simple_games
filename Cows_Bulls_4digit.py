
#cows and bulls game after video
# 4 digit number guessing game

import random
      
def instructions():
    print("Welcome to Cows and Bulls. Attempt to guess the 4 digit number")
    print("The number can have digits from 0 to 9 in any of the 4 positions")
    print("You get 1 Cow for each correct digit in any position in the number")
    print("You get 1 Bull for each correct digit in the correct position")
    print("You have 7 tries to guess the number")
    

def play_again():
    print("Do you want to play again?")
    question = input("Enter Y for yes, or N for no: ").upper()
    if question == "Y":
        play_game()
    else:
        print("Thank you for playing")

all_numbers = []
only_good = []
number = []

def make_number():
    all_numbers = list(range(1000, 9999))
    for i in range(0, len(all_numbers)):
        all_numbers[i] = str(all_numbers[i])

    for num in all_numbers:
        if len(num) == len(set(num)):
            only_good.append(num)
    
def get_number():
    number = random.choice(only_good)
    number = [int(d) for d in str(number)]
    return number
    
    
def play_game():
    instructions()
    make_number()
    number = get_number()
    
    remaining_try = 7
    while remaining_try > 0:
        
        choice = input("Enter 4 digits:")
        guess = []
        
        for i in range(4):
            guess.append(int(choice[i]))
            
        if choice == number:
            print("Congratulations! You Win!")
            break
        
        cows = 0
        bulls = 0
        
    
        for b in range(4):
            if guess[b] == number[b]:
                bulls += 1
        for c in range(4):
            for x in range (4):
                if guess[x] == number[c]:
                    cows += 1
                    
        print(bulls, "Bulls")
        print(cows, "Cows")
        if bulls == 4:
            print("You Win! The number was", number)
            play_again()
            
    
        remaining_try -= 1
        if remaining_try <= 0:
            print("Sorry better luck next time. The number was", number)
            play_again()

        
play_game()


