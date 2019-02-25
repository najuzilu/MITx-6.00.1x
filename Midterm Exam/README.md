## Problem 1-1 ##
Suppose x = "pi" and y = "pie". The line of code x, y = y, x will swap the values of x and y, resulting in x = "pie" and y = "pi".

**Answer**: True

## Problem 1-2 ##
Suppose x is an integer in the following code:
```python
def f(x):
	while x > 3:
    	f(x+1)
```
**Answer**: False

## Problem 1-3 ##
A Python program always executes every line of code written at least once.

**Answer**: False

## Problem 1-4 ##
Suppose you have two different functions that each assign a variable called x. Modifying x in one function means you always modify x in the other function for any x

**Answer**: False

## Problem 1-5 ##
The following code will enter an infinite loop for all values of i and j.
```python
while i >= 0:
    while j >= 0:
        print(i, j)
```
**Answer**: False

## Problem 1-6 ##
It is always possible and feasible for a programmer to come up with test cases that run through every possible path in a program.

**Answer**: False

## Problem 1-7 ##
Assume f() is defined. In the statement a = f(), a is always a function.

**Answer**: False

## Problem 1-8 ##
A program that keeps running and does not stop is an example of a syntax error.

**Answer**: False

## Problem 1-9 ##
Consider the following function.
```python
def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1)
```
A new object of type list is created for each recursive invocation of f

**Answer**: True

## Problem 1-10 ##
A tuple can contain a list as an element.

**Answer**: True

## Problem 2-1 ##
Consider the statement: L = {'1':1, '2':2, '3':3}. Which is correct?

**Answer**: L maps strings to integers

## Problem 2-2 ##
Assume a break statement is executed inside a loop and that the loop is inside a function. Which of the following is correct?

**Answer**: All of the above.
* The program might immediately terminate.
* The function might immediately terminate.
* The loop will always immediately terminate.

## Problem 2-3 ##
In Python, which of the following is a mutable object?

**Answer**: a list

## Problem 2-4 ##
Assume the statement s[1024] = 3 does not produce an error message. This implies:

**Answer**: type(s) can be list

## Problem 2-5 ##
Consider the code:
```python
L = [1,2,3]
d = {'a': 'b'}
def f(x):
    return 3
```

**Answer**:
```python
for i in range(1000001, -1, -2):
    print(f)
```

## Problem 2-6 ##
Examine the following code snippet:
```python
stuff  = _____
  for thing in stuff:
        if thing == 'iQ':
           print("Found it")
```
Select all the values of the variable "stuff" that will make the code print "Found it".

**Answer**: 
* ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
* ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
* ["iQ"]

## Problem 2-7 ##
The following Python code is supposed to compute the square of an integer by using successive additions.
```python
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x
```

**Answer**: Nothing is wrong; the code is fine as-is.

## Problem 3 ##
Implement a function called closest_power that meets the specifications below.
```python
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
```
For example,
* `closest_power(3,12)` returns 2
* `closest_power(4,12)` returns 2
* `closest_power(4,1)` returns 0
Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.

**Answer**:
```python
def closest_power(base, num):
	if base > num:
		return 0 # closest_power(4,1) == 0
	elif base == num:
		return 1 # closest_power(4,4) == 1
	else:
		# for all other cases
		for i in range(1, int(num)):
			current_ = base ** i - num
			next_ = base ** (i + 1) - num
			if abs(current_) <= abs(next_):
				return i
```

## Problem 4 ##
Write a function called `getSublists`, which takes as parameters a list of integers named L and an integer named n.
* assume L is not empty
* assume `0 < n <= len(L)`

This function returns a list of all possible sublists in L of length n without skipping elements in L. The sublists in the returned list should be ordered in the way they appear in L, with those sublists starting from a smaller index being at the front of the list.

Example 1, if `L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]` and `n = 4` then your function should return the list `[[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]`

Example 2, if `L = [1, 1, 1, 1, 4]` and `n = 2` then your function should return the list `[[1, 1], [1, 1], [1, 1], [1, 4]]`


Your function does not have to be recursive. Do not leave any debugging print statements when you paste your code in the box.

**Answer**:
```python
def getSublists(L, n):
	answer = []
	for i in range(0, len(L) - n + 1):
		answer.append(L[i: i+n])
	return answer
```

## Problem 5 ##
Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.
```python
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
```

**Answer**:
```python
def uniqueValues(aDict):
	removed_dup = {k:v for k,v in aDict.items() if list(aDict.values()).count(v)==1}
	return sorted(list(removed_dup.keys()))
```

## Problem 6 ##
Write a recursive Python function, given a non-negative integer N, to calculate and return the sum of its digits.

Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 10 removes the rightmost digit (126 // 10 is 12).

This function has to be recursive; you may not use loops!

This function takes in one integer and returns one integer.
```python
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
```

**Answer**:
```python
def sumDigits(N):
	if N < 10:
		return N
	else:
		return ((N%10) + sumDigits(N//10))
```

## Problem 7 ##
Write a Python function called `satisfiesF` that has the specification below. Then make the function call `run_satisfiesF(L, satisfiesF)`. Your code should look like:
```python
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here

run_satisfiesF(L, satisfiesF)
```
For your own testing of `satisfiesF`, for example, see the following test function f and test code:
```python
def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)
```
Should print:
```python
2
['a', 'a']
```
Paste your entire function satisfiesF, including the definition, in the box below. After you define your function, make a function call to `run_satisfiesF(L, satisfiesF)`. Do not define `f` or `run_satisfiesF`. Do not leave any debugging print statements.

**Answer**:
```python
def satisfiesF(L):
	L_copy = L.copy()
	for each in L_copy:
		if f(each) == False:
			L.remove(each)
	return len(L)
```