'''
is in
'''

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        return char == aStr
    array = sorted(list(set(aStr)))
    middle = array[len(array)//2]
    if char == middle:
        return True
    elif char < middle:
        array = array[:array.index(middle)]
        aStr = "".join(array)
        return isIn(char, aStr)
    else:
        array = array[array.index(middle):]
        aStr = "".join(array)
        return isIn(char, aStr)