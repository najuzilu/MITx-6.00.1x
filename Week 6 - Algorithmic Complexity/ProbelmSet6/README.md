## Problem 1 ##

1. The ONLY thing we are interested in when designing programs is that it returns the correct answer. **Answer**: False
2. When determining asymptotic complexity, we discard all terms except for the one with the largest growth rate. **Answer**: True
3. Bisection search is an example of linear time complexity. **Answer**: False
4. For large values of `n`, an algorithm that takes `20000n^2` steps has better time complexity (takes less time) than one that takes `0.001n^5` steps. **Answer**: True

## Problem 2 ##

1. Indirection, as talked about in lecture, means you have to traverse the list more than once. **Answer**: False
2. The complexity of binary search on a sorted list of n items is `O (log n)`. **Answer**: True
3. The worst case time complexity for selection sort is `O(n^2)`. **Answer**: True
4. The base case for the recursive version of merge sort from lecture is checking ONLY for the list being empty. **Answer**: False

## Problem 3 ##

1. `O(n)`
2. `O(n^c)`
3. `O(n)`
4. `O(n^c)`
5. `O(n^c)`
6. `O(n^c)`
7. `O(n log n)`
8. `O(1)`
9. `O(c^n)`
10. `O(c^n)`

## Problem 4 ##

1. **Answer**: `O(1)`
```python
def modten(n):
    return n%10
```

2. **Answer**: `O(len(n))`
```python
def multlist(m, n):
    '''
    m is the multiplication factor
    n is a list.
    '''
    result = []
    for i in range(len(n)):
        result.append(m*n[i])
    return result  
```

3. **Answer**: `O(log(n))`
```python
def foo(n):
    if n <= 1:
        return 1
    return foo(n/2) + 1
```

4. **Answer**: `O(n)`
```python
def recur(n):
    if n <= 0:
        return 1
    else:
        return n*recur(n-1)
```

5. **Answer**: `O(n^2)`
```python
def baz(n):
    for i in range(n):
        for j in range(n):
            print( i,j )
```

## Problem 5 ##
Here is code for linear search that uses the fact that a set of elements is sorted in increasing order:
```python
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
```
Consider the following code, which is an alternative version of `search`.
```python
def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False
```
**Answer**: `search` and `newsearch` return the same answers for lists `L` of length 0, 1, or 2.

## Problem 6 ##
```python
def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
```

1. **Answer**: Increasing

2. **Answer**: `O(n^2)`

3. **Answer**: `modSwapSort` now orders the list in descending order for all lists.
```python
def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
```

4. _Best and worst cases stay the same._