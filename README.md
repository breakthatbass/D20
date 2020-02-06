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

The program takes one mandatory argument and two more optional arguments.


The first argument is the type of die to roll (e.g. d20) which by default it rolls once.
The second argument is a number which tells the program the amount of rolls to do if there are more than one roll wanted.
The third is a modifier which is a number with a '+' or '-' in front of it.

```
$ python dice.py die
```
It might look something like this:
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