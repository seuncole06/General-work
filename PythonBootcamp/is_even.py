# Even or Odd Checker
# Description: Write a function that takes an integer and returns True if the number is even, and False if it is odd.

def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(n = 7))