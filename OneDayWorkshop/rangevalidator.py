def get_input():
    '''Asks user for input'''
    user_input = int(input('Please enter a number in  the range 10 to 40: '))
    value = user_input
    return value


def check_input(value, check):
    '''Check if input between 10 and 40'''
    if value in range(10, 40):
        check = 'valid'
    return check


def main():
    '''ask for user input until check input is true'''
    check = 'invalid'
    while check is 'invalid':
        value = get_input()
        check = check_input(value, check)
        print("Sorry, the number must be between 10 and 40.  Please try again.")
    print("You entered", value, ". This is a valid number.")


main()