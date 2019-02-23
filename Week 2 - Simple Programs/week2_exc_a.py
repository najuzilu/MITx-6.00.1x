print('Please think of a number between 0 and 100!')

low = 0
high = 100

def main(low, high):
    ans = (high + low) // 2
    print('Is your secret number {}?'.format(ans))
    input_ = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    if input_ == 'l':
        low = ans
        main(low, high)
    elif input_ == 'h':
        high = ans
        main(low, high)
    elif input_ == 'c':
        print('Game over. Your secret number was: {}'.format(ans))
        return
    else:
        print('Sorry I did not understand your input.')
        main(low, high)

main(low, high)