def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    answer = True
    for letter in secretWord:
    	if letter in lettersGuessed:
    		answer = answer and True
    	else:
    		answer = answer and False
    return answer

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed)) # >> False


secretWord = 'apple' 
lettersGuessed = ['e', 'a', 'k', 'k', 'r', 'o']
print(isWordGuessed(secretWord, lettersGuessed))