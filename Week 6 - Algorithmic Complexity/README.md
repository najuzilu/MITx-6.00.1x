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
    total = 0               # one op
    for i in range(1000):   # one op
        total += i          # two op

    while x > 0:            # one op to check
        x -= 1              # two op
        total += x          # two op

    return total            # one op
```
**Answer**:
* best: 1 + 3*1000 + 1 + 1 = 3003
* worst: 1 + 3 * 1000 + (1+2+2)*n + 1 + 1[for x=0] = 3003 + 5n
2. program 2
```python
def program2(x):
    total = 0               # one op
    for i in range(1000):   # one op
        total = i           # one op

    while x > 0:            # one op [also checks x=0]
        x = x//2            # two op
        total += x          # two op

    return total            # one op
```
**Answer**:
* best: 1+ 2*1000 + 1+1 = 2003
* worst: 1 + 2*1000 + 5*log2(n) + 5[x//2 takes all the way to x=1] + 1 + 1 = 2008 + 5*log2(n)
3. program 3
```python
def program3(L):
    totalSum = 0                    # one op
    highestFound = None             # one op
    for x in L:                     # one ops
        totalSum += x               # two ops

    for x in L:                     # one ops
        if highestFound == None:    # one op
            highestFound = x        # one op
        elif x > highestFound:      # one op
            highestFound = x        # one op

    return (totalSum, highestFound) # one op
```
**Answer**:
* best: L=0 => 1 + 1 + 1 = 3
* worst: 2 + 3n + [3 + 4(n-1)] + 1 = 7n + 2

#### Big Oh Notation ####

Big Oh notation meadures an **uper bound on the asymptotic growth**, often called order of growth  
Big Oh or O() is used to describe worst case
* worst case occurs often and is the bottleneck when a program runs
* express rate of growth of program relative to the input size
* evaluate algorithm not machine or implementation  
Examples:
1. n^2 + 2n + 2 : O(n^2)
2. n^2 + 10000n + 3^1000 : O(n^2)
3. log(n) + n + 4 : n
4. 0.0001 * n * log(n) + 300n : O(n log(n))
5. 2n^30 + 3^n : O(3^n)  
Complexity classes ordered low to high:
O(1) - constant
O(log n) - logarithmic
O(n) - linear
O(n log n) - loglinear
O(n^c) - polynomial
O(c^n) - exponential  
**Law of Addition** for O():
* used with **squential** statements
* O(f(n)) + O(g(n)) is O(f(n) + g(n))
* for example, O(n^2)
```python
for i in range(n):
    print('a')
for j in range(n*n):
    print('b')
```
**Law of Multiplication** for O():
* used with **nested** statements/loops
* O(f(n)) * O(g(n)) is O(f(n) * g(n))
* for example, O(n^2)
```python
for i in range(n):
    for j in range(n):
        print('a')
```

#### Exercise 3 ####
1. program 1:
```python
def program1(L):
    multiples = []                  # one op
    for x in L:                     # one op > n times
        for y in L:                 # one op >
            multiples.append(x*y)   # two op > 
    return multiples                # one op
```
**Best case**: 1 + 1 = 2  
**Worst case**: 1 + n + n * (3n) + 1 = 3n^2 + n + 2
2. program 2:
```python
def program2(L):
    squares = []                        # one op
    for x in L:                         # one op
        for y in L:                     # one op
            if x == y:                  # one op
                squares.append(x*y)     # two op
    return squares                      # one op
```
**Best case**: 2  
**Worst case**: 1 + n + (3n + n) * n + 1 = 2 + n + 4n^2
3. program 3:
```python
def program3(L1, L2):
    intersection = []                   # one op
    for elt in L1:                      # one op
        if elt in L2:                   # one op
            intersection.append(elt)    # one op
    return intersection                 # one op
```
**Best case**: 2  
**Worst case**: 1 + n * (n+2) + 1 = 2 + n^2 + 2n
4.
* O(n^2)
* O(n^2)
* O(n^2)

#### Exercise 4 ####
1. O(n)
2. O(n)
3. O(1)
4. O(n^2)

#### Complexity classes ####
* O(1) denotes constant running time
* O(log n) denotes logarithmic running time
* O(n) denotes linear running time
* O(n log n) denotes log-linear running time
* O(n^c) denotes polynomial running time
* O(c^n) denotes exponential running time

Logarithmic complexity:  
* complexity grows as log of size of one of its inputs
* example:
    * bisection search
    * binary search of a list
```python
def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i//10
    return result
```

Linear complexity:
* searching a list in sequence to see if an element is present
* add characters of a string, assumed to be composed of decimal digits
```python
def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val
```
* complexity can depend on number of recursive calls
```python
def fact_iter(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod
```
```python
def fact_recur(n):
    if n <= 1:
        return 1
    else:
        return n* fact_recur(n - 1)
```

Log-linear complexity:
* many practical algorithms are log-linear
* very commonly used log-linear algorithm is merge sort

#### Analyzing complexity ####

Polynomial complexity:
* most common polynomial algorithms are quadratic
* commonly occurs when we have nested loops or resursive function calls
```python
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
```

Exponential complexity:
* recursive function where more than one recursive call for each size of problem
```python
def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])

    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new
```

#### Exercise 6 ####
1. O(1)
2. O(b)
3. O(b)
4. O(log b)

#### Recursion Complexity ####
```python
def h(n):
    answer = 0
    s = str(n)
    for c in s:
        answer += int(c)
    return answer
```
**Answer**: O(log n)
* convert integer to string
* iterate over **length of string**, not magnitude of input n
* think of it like dividing n by 10 each iteration

```python
def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n-1):
            temp = fib_i
            fib_i = fib_ii
            fib_ii = temp + fib_ii
        return fib_ii
```
**Answer**: O(n)

```python
def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)
```
**Answer**: O(2^n)

**Complexity of common Python functions**
* Lists: `n` is `len(L)`
    * index     O(1)
    * store     O(1)
    * length    O(1)
    * append    O(1)
    * ==        O(n)
    * remove    O(n)
    * copy      O(n)
    * reverse   O(n)
    * iteration O(n)
    * in list   O(n)
* Dictionaries: `n` is `len(d)`
    * worst case
        * index         O(n)
        * store         O(n)
        * length        O(n)
        * delete        O(n)
        * iteration     O(n)
    * average case
        * index         O(1)
        * store         O(1)
        * delete        O(1)
        * iteration     O(n)

#### Exercise 7 ####
1. O(len(s))
2. O(log(len(s)))
3. O(n^2)
4. O(n^2)

#### Exercise 8 ####
1. 500,000
log log n
log n
n 
n * log n
n ** 2
n ** 3
3 ** n
n ** n
2 ** (n ** 2)

### Searching and Sorting Algorithms ###