import random
import sys

def main():
    print("Choose 1 for Rock, 2 for Paper, and 3 for Scissors")
    guess = int(input("Rock, Paper, Scissors, Shoot!"))
    bot = ai_guess()
    checkWin(guess, bot)
def ai_guess():
    bot = random.randint(1, 3)
    return bot
    bot = (p1)
    guess = (p2)

def checkWin(p1, p2):
    
    if (p1 == 1 and p2 == 2):
        print("Your oppenent chose rock, you win!")
    elif (p1 == 2 and p2 == 3):
        print("Your oppenent chose Paper, you win!")
    elif (p1 == 3 and p2 == 1):
        print("Your oppenent chose scissors, you win!")
    elif (p1 == p2):
        print("its a tie")
    elif (p1 == 3 and p2 == 2):
        print("Your oppenent chose scissors, you lose.")        
        
    elif (p1 == 2 and p2 == 1):
        print ("Your oppenent chose paper, you lose.")
    elif (p1 == 1 and p2 == 3):
        print("Your oppenent chose rock, you lose.")    
   
    
        

if __name__ == "__main__":
    main()