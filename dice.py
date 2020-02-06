import sys
from random import randint
from termcolor import colored
from helpers import check_die, roll_dice

def main():
    # show usage if not executed correctly
    if len(sys.argv) < 2:
        print()
        print(colored('Usage: ', 'red'), end='')
        print('python dice.py ', end='')
        print(colored('dice-type', 'cyan'))
        print()
        print('Optional Arguments:')
        print(colored('number-of-rolls', 'green'))
        print(colored('modifier', 'green'))
        print()
        return 1
    
    die = sys.argv[1]
    rolls = 1
    modifier = 0

    if len(sys.argv) == 3:
        rolls = int(sys.argv[2])

    if len(sys.argv) == 4:
        rolls = int(sys.argv[2])
        modifier = sys.argv[3]

    # check to see if user input is a valid die
    die = check_die(die)
    
    # if it is, roll it!
    roll_dice(die, rolls, modifier)

if __name__ == "__main__":
    main()