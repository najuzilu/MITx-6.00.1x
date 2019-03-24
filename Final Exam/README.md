## Final Exam ##

### Problem 1 ###

1. In the statement L = [1,2,3], L is a class. **Answer**: False
2. The orders of growth of `O(n^2+1)` and `O(n^5+1)` are both polynomial. **Answer**: True
3. The complexity of binary search on a sorted list of n items is `O(logn)`. **Answer**: True
4. A bisection search algorithm always returns the correct answer when searching for an element in a sorted list.**Answer**: True
5. Performing binary search on an unsorted list will always return the correct answer in `O(n)` time where  is the length of the list. **Answer**: False

### Problem 2 ###

1. Which of the following is correct?
```python
class A(object):
	def foo(self):
		print('hi')

class B(A):
	def foo(self):
		print('bye')
```
**Answer**: When a = A() we say that a is an instance of A

2. Consider the function f below. What is its Big O complexity?
```python
def f(n):
    def g(m):
        m = 0
        for i in range(m):
            print(m)
    for i in range(n):
        g(n)
```
**Answer**: `O(n)`

3. A dictionary is an immutable object because its keys are immutable. **Answer**: False because a dictionary is mutable

4. Consider the following two functions and select the correct choice below:
```python
def foo_one(n):
    """ Assume n is an int >= 0 """
    answer = 1.0
    while n > 1:
        answer *= n
        n -= 1
    return answer

def foo_two(n):
    """ Assume n is an int >= 0 """
    if n <= 1: 
        return 1.0
    else: 
        return n*foo_two(n-1)
```
**Answer**: The worst case Big Oh time complexity of `foo_one` and `foo_two` are the same.

5. The complexity of `1^n + n^4 + 4n + 4` is: **Answer**: polynomial

### Problem 3 ###

Write a Python function that takes in a string and prints out a version of this string that does not contain any vowels, according to the specification below. Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

For example, if `s = "This is great!"` then print_without_vowels will print `Ths s grt!`. If `s = "a"` then print_without_vowels will print the empty string.
```python
def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels.extend([_.upper() for _ in vowels])
    output = ''
    for char in s:
    	if char not in vowels:
    		output += str(char)
    print(output)
```