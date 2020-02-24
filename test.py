import pytest
import sys

from helpers import check_die
from dice import main

def test_die():
    assert check_die("d4") == 4
    assert check_die("d6") == 6
    assert check_die("d8") == 8
    assert check_die("d10") == 10
    assert check_die("d12") == 12
    assert check_die("d20") == 20
    assert check_die("d5") ==  1
    assert check_die("234fdsdf") == 1
    assert check_die("d3") ==  1

