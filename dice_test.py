import pytest
from helpers import check_die

@pytest.mark.parametrize('die, expected', 
[('d4', 4), ('d6', 6), ('d8', 8), ('d10', 10), ('d12', 12), ('d20', 20)]) 
def test_die(die, expected):
    assert check_die(die) == expected

### PASSED ###

def test_exit():
    with pytest.raises(SystemExit):
        check_die('d2')
        check_die('d3')
        check_die('20')
        check_die('sd4rfwf')
        check_die('d4w')
        check_die('4')
        check_die('6')
        check_die('8')
        check_die('10')
        check_die('12')
        check_die('')


