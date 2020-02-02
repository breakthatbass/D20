import sys
from random import randint

def main():
    if len(sys.argv) != 3:
        print("Usage: python dice.py dice-type rolls")
    
    die = int(sys.argv[1])
    rolls = int(sys.argv[2])

    for i in range(rolls):
        cast = randint(1, die)

        if cast == 20:
            print("Roll {} is 20! Critical Hit!".format(i + 1))
        elif cast == 1 and die == 20:
            print("Roll {} is 1. Critical miss! Dangit!".format(i + 1))
        else:
            print("Roll {} is {}".format(i + 1, cast))

if __name__ == "__main__":
    main()