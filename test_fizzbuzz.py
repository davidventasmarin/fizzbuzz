from fizzbuzz import fizz


def test_divisible3():
    assert fizz(3) == "Fizz"
    assert fizz(6) == "Fizz"
    assert fizz(9) == "Fizz"

def test_divisible5():
    assert fizz(5)  == "Buzz"
    assert fizz(10) == "Buzz"