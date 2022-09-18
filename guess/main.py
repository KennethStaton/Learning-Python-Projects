import random

def guess(x): # Function where user inputs a number
    random_number = random.randint(1, x)
    guess = 0 # while loop will never be broken for the guess
    while guess != random_number:
        #fstring where the integer is not a word but a number, hence int = number, input = needing from user
        guess = int(input(f'Guess a number between 1 and {x}: ')) 
        if guess < random_number:
            print("Sorry your guess is to low")
        elif guess > random_number: #elif is fine here
            print("Sorry your guess is to high")
    #While loop conditions are broken out of, so user has made correct guess
    #Indenting made random_number undefined. Very important in this language        
    print(f"Congrats! You have guessed the number {random_number}! ")


def computer_guess(x):
    low = 1
    high = x #setting range for computer to guess
    feedback = '' #feedback open character for while loop insertion
    while feedback != 'c':
        if low != high:
            random_guess = random.randint(low, high)
        else:
            random_guess = low
        feedback = input(f'Is {random_guess} too high (H), too low(L), or Correct (C)').lower() #how to make user inputs not case sensitive
        
        #Overall goal is to make the computers bounds of guessing lower for higher change of guessing
        if feedback == 'h':
            high = random_guess - 1
        elif feedback == 'l':
            low = random_guess + 1
            
    print(f"Haha I knew I would get the correct answer of {random_guess}. I am a super smart AI")
            
computer_guess(10)
#Lesson: Indentions are very important. You need to feed it the bounds on the same level of the function
