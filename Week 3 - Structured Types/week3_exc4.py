def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))
    

    lettersGuessed = []
    guesses = 8
    
    while (guesses > 0):

        print('-------------')

        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
            return
        else:
            print('You have {} guesses left.'.format(guesses))
            print('Available letters: {}'.format(getAvailableLetters(lettersGuessed)))
            guessChar = input('Please guess a letter: ')

            if guessChar not in lettersGuessed:
                lettersGuessed.append(guessChar)
            else:
                print('Oops! You\'ve already guessed that letter: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
                continue
            if guessChar in secretWord:
                print('Good guess: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
            else:
                print('Oops! That letter is not in my word: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
                guesses -= 1
    print('-------------')
    print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))