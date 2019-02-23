'''
Power iter
'''

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    answer = 1
    if exp == 0:
        return 1
    else:
        while(exp > 0):
            answer = answer * base
            exp -= 1
    return answer