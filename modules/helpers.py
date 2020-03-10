import sys
from random import randint
from termcolor import colored

def check_die(die):
    ''' take the die string and return it's value as int '''

    # dict to compare input to
    dice = {
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
        raise SystemExit(1)


def roll_dice(die, rolls, modifier):
    '''
     take die int, call randint() rolls amount, add the modifier to each roll
    '''
    print('----------------')
    for i in range(rolls):
        cast = randint(1, die)
        
        # Kepp track of crit to use to not show base and modifier if they are implemented    
        crit = False 
    
        if cast == 20: # crit hit true
            crit = True

        if cast == 1 and die == 20: # crit miss true
            crit = True

        # print info about rolls is there is a modifier
        if modifier != 0 and crit == False:
            print(f'base cast is {cast}')
            print(f"modifier is {modifier}")
    
        # account for crit hits and crits misses while rolling a d20
        if cast == 20:
            print(colored(f"Roll {i + 1} is 20! Critical Hit!", 'green', attrs=['bold']))
        elif cast == 1 and die == 20:
            print(colored(f"Roll {i + 1} is 1. Critical miss! Dangit!", 'red', attrs=['bold']))

        # if the modifer makes the roll go below 1, print 1
        elif cast + (int(modifier)) < 1:
            print(colored(f"Roll {i + 1} is 1", 'cyan'))
        # otherwise just do the math and print the value
        elif modifier != 0:
            print(colored(f"Roll {i + 1} is {cast + (int(modifier))}", 'cyan'))
        else:
            print(colored(f"Roll {i + 1} is {cast}", 'cyan'))
    
        print('----------------')