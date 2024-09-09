import random

def guessthenumber(min, max):
    answer=generateNum(min,max)

    #initialize the guess
    guess=None
    while guess!=answer:
        guess = int(input("Guess the Number\n"))
        if guess!=answer:
            print("Try again!")

    print(f"You're correct the answer is {guess}")

def generateNum(min, max):
    return random.randint(min, max)

guessthenumber(1,10)