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

### Problem 4 ###
Write a Python function that takes in two lists and calculates whether they are permutations of each other. The lists can contain both integers and strings. We define a permutation as follows:

* the lists have the same number of elements
* list elements appear the same number of times in both lists

If the lists are not permutations of each other, the function returns False. 
If they are permutations of each other, the function returns a tuple consisting of the following elements:

* the element occuring the most times
* how many times that element occurs
* the type of the element that occurs the most times

If both lists are empty return the tuple `(None, None, None)`. If more than one element occurs the most number of times, you can return any of them.

```python
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    answer = {}
    if len(L1) == len(L2):
    	if len(L1) == 0:
    		return (None, None, None)
    	set_L1 = set(L1)
    	set_L2 = set(L2)
    	if set_L1 == set_L2:
    		for elem in set_L1:
    			if L1.count(elem) == L2.count(elem):
    				answer[elem] = L1.count(elem)
    			else:
    				return False
    	else:
    		return False
    else:
    	return False
    output = [(k, v) for k, v in answer.items() if v == max(answer.values())][0]
    return (output[0], output[1], type(output[0]))
```

For example,
* if `L1 = ['a', 'a', 'b']` and `L2 = ['a', 'b']` then `is_list_permutation` returns `False`
* if `L1 = [1, 'b', 1, 'c', 'c', 1]` and `L2 = ['c', 1, 'b', 1, 1, 'c']` then `is_list_permutation` returns `(1, 3, <class 'int'>)` because the integer 1 occurs the most, 3 times, and the type of 1 is an integer (note that the third element in the tuple is not a string).

### Problem 5 ###

You are given a dictionary aDict that maps integer keys to integer values. Write a Python function that returns a list of keys in aDict that map to dictionary values that appear exactly once in `aDict`.

* This function takes in a dictionary and returns a list.
* Return the list of keys in increasing order.
* If `aDict` does not contain any values appearing exactly once, return an empty list.
* If `aDict` is empty, return an empty list.

For example:
If` aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}` then your function should return `[1, 3, 8]`
If `aDict = {1: 1, 2: 1, 3: 1}` then your function should return `[]`

```python
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    output = []
    list_values = list(aDict.values())
    
    for k, v in aDict.items():
    	if list_values.count(v) == 1:
    		output.append(k)
   	output.sort()
    return output

```