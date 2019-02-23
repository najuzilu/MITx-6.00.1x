#### Classes of Tests ####

* Unit testing
	* validate each piece of program
	* testing each function separately

* Regression testing
	* add test for bugs as you find them in a funtion
	* catch reintroduced errors that were previously fixed

* Integration testing
	* does overall program work?
	* tend to rush to do this

#### Testing approaches ####

```python
def is_bigger(x, y):
	'''Assumes x and y are ints
	Returns True if y is less than x, else False'''
```

* Black box testing - explore paths through specification
	* designed without looking at the code
	* can be done by someone other than the implementer to avoid some implementer biases
	* testing can be refused if implementation changes
	* paths through specification
		* build test cases in different natural space partition
		* also consider boundary conditions (empty lists, sinleton list, large number, small number)

* Glass box testing - explore paths through code
	* use code directly to guide design of test cases
	* called path-complete if every potential path through code is tested at least once
	* what are some drawbacks of this type of testing?
		* can go through loops arbitrarily many times
		* missing paths
	* guidelines
		* branches (exercise all parts of a condition)
		* for loops (loop not entered, body of loop executed extacly once, body of loop executed more than once)
		* while loops (same as for loops, cases that catch all ways to exit loop)

example:
```pyhon
def abs(x):
	''' Assumes x is an int
	Returns x if x>=0 and -x otherwise'''
	if x < -1:
		return -x
	else:
		return x
```
* a path-complete test suite could miss a bug
* path-complete test suite: 2 and -2
* but abs(-1) incorrectly returns -1
* should still test boundary cases