import sys
from random import randint
from termcolor import colored

def main():
    if len(sys.argv) < 3:
        print("Usage: python dice.py dice-type rolls modifier")
        return 1
    
    die = int(sys.argv[1])
    rolls = int(sys.argv[2])
    modifier = 0

    if len(sys.argv) == 4:
        modifier = sys.argv[3]
    
    def roll_dice(die, rolls, modifier):
        
        print('----------------')
        for i in range(rolls):
            cast = randint(1, die)
            
            if modifier != 0 and cast > 1 and cast < 20:
                print(f'base cast is {cast}')
                print(colored(f"modifier is {modifier}", 'blue'))
            
            if cast == 20:
                print(colored(f"Roll {i + 1} is 20! Critical Hit!", 'green'))
            elif cast == 1 and die == 20:
                print(colored(f"Roll {i + 1} is 1. Critical miss! Dangit!", 'red'))
            else:
                print(f"Roll {i + 1} is {cast + (int(modifier))}")
            print('----------------')

    roll_dice(die, rolls, modifier)

if __name__ == "__main__":
    main()