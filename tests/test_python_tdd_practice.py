from python_tdd_practice.calc import Calc

def test_add_two_numbers():
    c = Calc()
    res = c.add(4, 5)
    assert res == 9

def test_add_three_numbers():
    c = Calc()
    res = c.add(4, 5, 10)
    assert res == 19

def test_add_many_numbers():
    s = range(100)
    assert Calc().add(*s) == 4950

def test_subtrace_two_numbers():
    c = Calc()
    res = c.sub(10, 3)
    assert res == 7

def test_mul_two_numbers():
    c = Calc()
    res = c.mul(1, 5)
    assert res == 5

def test_mul_many_numbers():
    s = range(1, 10)
    assert Calc().mul(*s) == 362880
    
def test_div_two_numbers():
    c = Calc()
    res = c.div(11, 5)
    assert res == 2.2
