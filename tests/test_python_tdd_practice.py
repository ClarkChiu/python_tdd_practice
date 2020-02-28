from python_tdd_practice.calc import Calc

def test_add_two_numbers():
    c = Calc()
    res = c.add(4, 5)
    assert res == 9

def test_add_three_numbers():
    c = Calc()
    res = c.add(4, 5, 10)
    assert res == 19
