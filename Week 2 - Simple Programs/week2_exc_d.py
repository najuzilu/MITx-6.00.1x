'''
gcd iter
'''

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    min_val = min(a,b)
    while(min_val):
        if (a % min_val == 0) and (b % min_val == 0):
            return min_val
        else:
            min_val -= 1
    
