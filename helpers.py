import sys
from termcolor import colored

def check_die(die):
    # dict to compare input to
    dice = {
        "d3": 3,
        'd4': 4,
        'd6': 6,
        'd8': 8,
        'd10': 10,
        'd12': 12,
        'd20': 20
        }
    # check to see if arg matches any element in dict
    for el in dice:
        if die == el:
            die = dice[el]
            return die

    # if not, exit the program and show correct usage
    if type(die) == str:
        print(colored('Not a valid die', 'blue'))
        print(colored('Valid Dice:', 'green'))
        for el in dice:
            print(el)
        sys.exit(1)