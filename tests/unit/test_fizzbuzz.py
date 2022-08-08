import pytest
from LeetCode.fizzbuzz.fizzbuzz import Solution

def test_fizzbuzz_3():
    expected = ['1','2','Fizz']
    blank = Solution()
    actual = blank.fizzBuzz(3)
    assert actual == expected



def test_fizzbuzz_5():
    expected = ['1','2','Fizz', '4', 'Buzz']
    blank = Solution()
    actual = blank.fizzBuzz(5)
    assert actual == expected


def test_fizzbuzz_15():
    expected = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    blank = Solution()
    actual = blank.fizzBuzz(15)
    assert actual == expected

