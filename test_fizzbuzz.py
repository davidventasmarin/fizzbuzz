from fizzbuzz import fizz


def test_divisible3():
    assert fizz(3)  == "Fizz"
    assert fizz(6)  == "Fizz"  
    assert fizz(9)  == "Fizz"

def test_divisible5():
    assert fizz(5)  == "Buzz"
    assert fizz(10) == "Buzz"
    assert fizz(20) == "Buzz"

def test_divible_3_5():
    assert fizz(15) == "FizzBuzz"
    assert fizz(30) == "FizzBuzz"
    assert fizz(45) == "FizzBuzz"

def test_no_divisible():
    assert fizz(4)  == 4
    assert fizz(7)  == 7
    assert fizz(1)  == 1
    assert fizz(16) == 16

def test_contiene_3():
    assert fizz(32) == "Fizz"
    assert fizz(73) == "Fizz"
    assert fizz(63) == "Fizz"

def test_contiene_5():
    assert fizz(65) == "Buzz"
    assert fizz(52) == "Buzz"
    assert fizz(58) == "Buzz"

def test_contiene_3_5():
    assert fizz(35) == "FizzBuzz"
    assert fizz(53) == "FizzBuzz"
