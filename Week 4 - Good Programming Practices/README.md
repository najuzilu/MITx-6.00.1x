## Testing and Debugging ##

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

#### Runtime bugs ####
* Overt vs covert:
	* _Overt_ has an obvious manifestation - code crashed or runs forever
	* _Covert_ has no obvious manifestation - code returns a value, which may be incorrect but hard to determine
* Persistent vs intermittent:
	* _Persistent_ occurs every time code is run
	* _Intermittent_ only occurs some times, even if run on same input

Categories:
* Overt and persistent
	* Obvious to detect
	* Good programmers use _defensive programming_ to try to ensure that if error is made, bug will fall into this category
* Overt and intermittent
	* More frustrating, can be harder to debug, but if conditions that prompt bug can be reproduced, can be handled
* Covert
	* Highly dangerous, as users may not realize answers are incorrect until code has been run for long period

## Exceptions and Assertions ##

* Exceptions - what happens when procedure execution hits an unexpected condition?

Example exception usage:
```python
while True:
	try:
		n = input('Please enter an integer: ')
		n = int(n)
		break
	except ValueError:
		print('Input not an integer; try again')
	print('Correct input of an integer!')
```

Example: control inputs
```python
data = []
file_name = input('Provide a name of a file of data ')

try:
	fh = open(file_name, 'r')
except IOError:
	print('cannot open', file_name)
else:
	for new in fh:
		if new != '\n':
			addIt = new[:-1].split(',')
			data.append(addIt)
finally:
	fh.close()

gradeData = []
if data:
	for student in data:
		try:
			name = student[:-1]
			grades = int(student[-1])
			gradesData.append([name, [grades]])
		except ValueError:
			gradesData.append(student[:], [])
```

Example: raising an exception
```python
def get_ratios(L1, L2):
	''' Assumes: L1 and L2 are lists of equal length of numbers
		Returns: a list containing L1[i]/L2[i] '''
	ratios = []
	for index in range(len(L1)):
		try:
			ratios.append(L1[index]/float(L2(index)))
		except ZeroDivisionError:
			ratios.append(float('NaN'))
		except:
			raise ValueError('get_ratios called with bad arg')
	return ratios
```

## Assertions ##
* want to be sure that assumptions on state of computation are as expected
* user an _assert statement_ to raise an `AssertionError` exception if assumptions not met
* an example of good _defensive programming_

Example
```python
def avg(grades):
	assert not len(grades) == 0, 'no grades data'
	return sum(grades)/len(grades)
```

###### Assertions as defensive programming ######
* assertions don't allow a programmer to control response to unexpected conditions
* ensure that execution halts whenever an expected condition is not met
* typically used to check inputs to functions procedures, but can be used anywhere
* can be used to check output of a function to avoid propagating bad values
* can make it easier to locate a source of a bug