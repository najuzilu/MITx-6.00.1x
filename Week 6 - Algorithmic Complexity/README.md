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

**Search Algorithm** - algorithm where I want to find an element, or an item, or a group of items with specific properties within a much larger collection of items.
* Collection could be implicit:
    * example: find square root in a search problem
* Collection could be explicit:
    * example: is a student record stored in a collection of data

Search Algorithm:
* linear search
    * **brute force** search
    * list does not have to be sorted
* bisection search
    * list **MUST be sorted** to give correct answer

Linear Search on Unsorted List:
```python
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found
```

Linear Search on Sorted List:
```python
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
```

Bisection Search Implementation 1 - O(n log n):
```python
def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1( L[:half], e)
        else:
            return bisect_search1( L[half:], e)
```

Bisection Search Implementation 2 - O(log n):
```python
def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)
```

_When does it make sense to **sort first then search**?_  
* SORT + O(log n) < O(n) --> SORT < O(n) - O(log n)
* when sorting is less than O(n) --> never true!

Amortized Cost:
* why bother sorting first?
* in come cases, may sort a list once then do many searches
* **AMORTIZED cost** of the sort over many searches
* SORT + K * O(log n) < K * O(n) --> for large K, **SORT time becomes irrelevant**

### Bogo Sort ###
Aka monkey sort, bogosort, stupid sort, slowsort, permutation sort, shotgun sort
* Randomly assign numbers in list, check to see if they're sorted, if not, randomly assign numbers in list

```python
def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)
```
* Best case: O(n) where n is len(L) to check if sorted
* Worst case: O(?) it is unbounded if really unlucky

### Bubble Sort ###
* **compare consecutive pairs** of elements
* **swap elements** in pair such that smaller is first
* when reach end of list, **start over** again
* stop when **no more swps** have been made

```python
def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
```
* **O(n^2) where n is len(L)** to do len(L)-1 comparisons and len(L)-1 passes

### Selection Sort ###
* loop invariant
    * given a prefix of list L[0:i] and suffix L[i+1:len(L)], then prefix is sorted and no element in prefix is larger than smallest element in suffix
        1. base case: prefix empty; suffix whole list - invariant true
        2. induction step: move minimum element from suffix to end of prefix. Since invariant true before move, prefix sorted after append
        3. when exit, prefix is entire list, suffix empty, so sorted

```python
def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
```
Complexity of selection sort is **O(n^2) where n is len(L)**

### Merge Sort ###
* use a divide-and-conquer approach
    1. if list is of length 0 or 1, already sorted
    2. if list has more than one element, split into two lists, and sort each
    3. merge sorted sublists
        1. look at first element of each, move smaller to end of the result
        2. when one list is empty, just copy rest of other list

Example of merging:
| Left in list 1 | Left in list 2 | Compare  | Result |
| ------------- |:-------------:| -----:| -----:|
| [1,5,12,18,19,20] | [2,3,4,17] | 1,2 | [] |
| [5,12,18,19,20] | [2,3,4,17] | 5,2 | [1] |
| [5,12,18,19,20] | [3,4,17] | 5,3 | [1,2] |
| [5,12,18,19,20] | [4,17] | 5,4 | [1,2,3] |
| [5,12,18,19,20] | [17] | 5,17 | [1,2,3,4] |
| [12,18,19,20] | [17] | 12,17 | [1,2,3,4,5] |
| [18,19,20] | [17] | 18,17 | [1,2,3,4,5,12] |
| [18,19,20] | [] | 18,-- | [1,2,3,4,5,12,17] |

```python
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result
```
* go through two lists, only one pass
* compare only **smallest elements in each sublist**
* O(len(left) + len(right)) copied elements
* O(len(longer list)) comparisons
* **linear in length of the list**

Merge sort algorithm -- recursive:
```python
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
```
* at **first level of recursion level**
    * n/2 elements in each list
    * O(n) + O(n) = O(n) where n is len(L)
* at **second recursion level**
    * n/4 elements in each list
    * two merges --> O(n) where n is len(L)
* each recursion level is O(n) where n is len(L)
* **dividing list in half** with each recursive call
    * O(log(n)) where n is len(L)
* overall complexity is **O(n log n) where n is len(L)**


### Exercise 7 ###
**Application A:**

Every time it's asked to, it performs a linear search through list L to find whether it contains x.

**Application B:**

Sort list L once before doing anything else (using mergeSort). Whenever it's asked to find x in L, it performs a binary search on L.

1. If the application is asked to find x in L exactly one time, what is the worst case time complexity for Application A?  
**Answer**: O(n)

2. If the application is asked to find x in L exactly one time, what is the worst case time complexity for Application B?  
**Answer**: O(n log n)

3. If the application is asked to find x in L k times, what is the worst case time complexity for Application A?  
**Answer**: O(kn)

4. If the application is asked to find x in L k times, what is the worst case time complexity for Application B?  
**Answer**: O(n log n + k log n)

5. What value(s) of k would make Application A be faster (i.e., asymptotically grow slower than) Application B?  
**Answer**: k = 1  
**Explanation**: When k = 1, A's complexity is O(kn)=O(n), B's complexity is O(n log n + k log n) = O(n log n + log n)

6. What value(s) of k would make Application A grow at the same rate as Application B?  
**Answer**: k = log n  
**Explanation**: When k = log n, A's complexity is O(kn)=O(n log n) and B's complexity is O(n log n + k log n) = O(n log n + log n log n). log n log n grows slower than n log n, so in this case B's complexity is O(n log n).