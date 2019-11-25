#!/usr/bin/env python
# coding: utf-8

# Part 1 - Implement the Fibonacci sequence -
# Write a function in recursion.py, called fibonnaci, which will accept one integer 
# parameter (lets call it n) and returns the nth element of the Fibonnaci sequence.

def fibonacci(n):
    if n < 0:
        print ("Please enter a valid number.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
# test function    
print (fibonacci(9))
    
    
# Part 2 - Implement Euclid's GCD Algorithm - 
# Write a recursive function called gcd that takes parameters a and b and returns 
# their greatest common divisor.

def gcd(x, y):
    if y == 0:
        return x 
    else:
        return gcd(y, x%y)
    
# test function
print (gcd(36, 10))


# Part 3 - String comparison - 
# recursively. Write a function called compareTo(s1, s2) that
# will:
# • a negative number if s1 < s2,
# • 0 if s1 == s2, and
# • a positive number if s1 > s2

def compareTo(s1, s2): 
    if not s1 and not s2:
        return 0
    elif not s1:
        return -1
    elif not s2:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])

print (compareTo('shortstr', 'longstring'))
print (compareTo('same', 'same'))
print (compareTo('longstring', 'shortstr'))
