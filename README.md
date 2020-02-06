# D20

D20 is a program that rolls dice for dungeons and dragons

### Usage:

The program takes at least two or three arguments, the first is the type of die to roll (e.g. 20 for a D20) and the second is how many rolls.
The third is the modifier which would look something like '+2' or '-2'. 

If there's no modifier the third argument can be left out.

```
$ python dice.py dice rolls modifier
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