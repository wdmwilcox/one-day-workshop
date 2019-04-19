def create_rooms():
    '''generate a dictionary containing course numbers and the room numbers'''
    rooms = {'CS101' : '3004',
             'CS102' : '4501',
             'CS103' : '6755',
             'NT110' : '1244',
             'CM241' : '1411'}
    return rooms


def create_instructors():
    '''generate a dictionary containing course numbers and the instructor names'''
    instructors = {'CS101' : 'Haynes',
                   'CS102' : 'Alvarado',
                   'CS103' : 'Rich',
                   'NT110' : 'Burke',
                   'CM241' : 'Lee'}
    return instructors


def create_times():
    '''generate a dictionary containing course numbers and the meeting times'''
    times = {'CS101' : '8:00 a.m.',
             'CS102': '9:00 a.m.',
             'CS103': '10:00 a.m.',
             'NT110': '11:00 a.m.',
             'CM241': '1:00 p.m.'}
    return times

def help_student(rooms, instructors, times):
    course_number = str(input("Please enter a course number:"))
    if course_number in rooms.keys():
        try:
            print("Room Number is" + rooms[course_number])
            print("Instructor is" + instructors[course_number])
            print("Meeting Time is" + times[course_number])
        except Exception:
            print("That room is not in the list.")
    else:
        print("That's not a  real course.")


def main():
    try:
        rooms = create_rooms()
    except Exception:
        "Error, create room dictionary failed"

    try:
        instructors = create_instructors()
    except Exception:
        "Error, create instructors dictionary failed"

    try:
        times = create_times()
    except Exception:
        "Error, create times dictionary failed"

    print("Welcome to the University Course Helper for Students who can't help themselves")
    print("Choose from among the following courses:")
    for key in rooms:
        print(key)

    done = 'n'
    while done != 'y':
        try:
            help_student(rooms, instructors, times)
        except Exception:
            print("I just can't help you")

        done = input("Are you finished?  y or n ")
        if done == 'y':
            print('Good riddance')
        else:
            print("Let's  try again..")


main()
