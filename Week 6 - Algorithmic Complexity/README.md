## Algorithmic Complexity ##

### Computational Complexity ###

How can we decide which option for program is most efficient? 
* We separate **time and space efficiency** of a program
* tradeoff between them - will focus on time efficiency  
Challenges in understanding efficiency of solution to a computational problem:
* a program can be implemented in many different ways
* you can solve a problem using a handful of different algorithms  
How to evaluate efficiency of programs?
* measure with a **timer**
* **count** the operations
* abstract notion of **order of growth**  
Timing programs is inconsistent:
* GOAL: to evaluate different algorithms
* running time **varies between algorithms**
* running time **varies between implementations**
* running time **varies between computers**
* running time is **predictable** based on small inputs  
_Time varies for different inputs but cannot really express a relationship between inputs and time_  
Counting operations:
* count **depends on algorithm**
* count **depends on implementations**
* count **independent of computers**
* no real definition of **which operations** to count  
_Count varies for different inputs and can come up with a relationship between inputs and the count_  
Need to choose which input to use to evaluate a function  
* want to express efficiency in terms of input, so need to decide what your input is
* could be an integer
* could be the length of list
* you decide when multiple parameters to a function  
Suppose you are given a list `L` of some length `len(L)`
* **best case**: minimum running time over all possible inputs of a given size, len(L)
* **average case**: average running time over all possible inputs of a given size, `len(L)` _practical measure_
* **worst case**: maximum running time over all possible inputs of a given size, `len(L)`  
Types of orders of growth:
* constant
* linear
* quadratic
* log
* n log n
* exponential

#### Exercise 1 ####
```python
def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False
```
1. Best Case Run Time: `linearSearch([20, 10, 1, 7, 4, 22, 25, 12, 31], 20)`
2. Worst Case Run Time: `linearSearch([13, 9, 22, 3, 10, 17, 11, 2, 12], 26)`
3. Average Case Run Time: `linearSearch([9, 3, 12, 24, 7, 8, 23, 11, 19], 8)`
4. What is the number of steps it will take to run `linearSearch` in the best case? Express your answer in terms of `n`, the number of elements in the list `L`.
* 1
* 2n + 1

#### Exercise 2 ####
1. program 1
```python
def program1(x):
    total = 0
    for i in range(1000): 
        total += i

    while x > 0:
        x -= 1
        total += x

    return total
```
**Answer**:
* best: 3003
* worst: 5n + 3003
2. program 2
```python
def program2(x):
    total = 0
    for i in range(1000):
        total = i

    while x > 0:
        x = x//2
        total += x

    return total
```
**Answer**:
* best:
* worst:
3. program 3
```python
def program3(L):
    totalSum = 0
    highestFound = None
    for x in L:
        totalSum += x

    for x in L:
        if highestFound == None:
            highestFound = x
        elif x > highestFound:
            highestFound = x

    return (totalSum, highestFound)
```
**Answer**:
* best:
* worst:

### Searching and Sorting Algorithms ###