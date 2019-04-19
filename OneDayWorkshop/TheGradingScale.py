
def long_way():
    '''nested if statements'''
    number_grade = int(input("Enter number grade:"))
    if number_grade >= 96:
        letter_grade = 'A+'
    else:
        if number_grade >= 90:
            letter_grade = 'A'
        else:
            if number_grade >= 87:
                letter_grade = 'B+'
            else:
                if number_grade >= 81:
                    letter_grade = 'B'
                else:
                    if number_grade >= 79:
                        letter_grade = 'B-'
                    else:
                        if number_grade >= 77:
                            letter_grade = 'C+'
                        else:
                            if number_grade >= 71:
                                letter_grade = 'C'
                            else:
                                if number_grade >= 69:
                                    letter_grade = 'C-'
                                else:
                                    if number_grade >= 67:
                                        letter_grade = 'D+'
                                    else:
                                        if number_grade >= 60:
                                            letter_grade = 'D'
                                        else:
                                            letter_grade = 'F'
    return letter_grade


def short_way():
    '''uses elifs'''
    number_grade = int(input("Enter number grade:"))
    if number_grade >= 96:
        letter_grade = 'A+'
    elif number_grade >= 90:
        letter_grade = 'A'
    elif number_grade >= 87:
        letter_grade = 'B+'
    elif number_grade >= 81:
        letter_grade = 'B'
    elif number_grade >= 79:
        letter_grade = 'B-'
    elif number_grade >= 77:
        letter_grade = 'C+'
    elif number_grade >= 71:
        letter_grade = 'C'
    elif number_grade >= 69:
        letter_grade = 'C-'
    elif number_grade >= 67:
        letter_grade = 'D+'
    elif number_grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    return letter_grade


def main():
    letter_grade = long_way()
    print("Letter grade is ", letter_grade, ", and you used the long way")
    letter_grade = short_way()
    print("Letter grade is ", letter_grade, ", and you used the short way")

main()
