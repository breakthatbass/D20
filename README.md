# D20

D20 is a program that rolls dice for dungeons and dragons

### Installation
```
$ git clone https://github.com/breakthatbass/D20.git
```
then
```
cd D20 or cd path/to/D20
```

### Usage:

This program takes one mandatory argument and two optional arguments.


The first argument is the type of die to roll (e.g. d20) which by default it rolls once.


The second argument is a number which tells the program the amount of rolls to do if there are more than one roll wanted.


The third argument is a modifier which is a number with '+' or '-' in front of it.


run with one of 6 dice: d4, d6, d8, d10, d12, d20

```
$ python dice.py die
```
or with additional arguments
```
$ python dice.py die rolls modifier
```

#### Example (with all three arguments):
```
$ python dice.py d20 3 +3
```
which might return something like:

```
-----------
Base roll is 7
Modifier is +3
Roll 1 is 9.
-----------
Roll 2 is 20. Critical hit!
-----------
Base roll is 13
Modifier is +3
Roll 3 is 16
-----------
```