def create_answer_key():
    '''create a list with the correct answers'''
    answer_key = ['A', 'B', 'A', 'C', 'C', 'C', 'D', 'B', 'A', 'A', 'C', 'B', 'A', 'C', 'A', 'D', 'D', 'B', 'D', 'A']
    return answer_key


def create_random_answers():
    '''create a random list of answers'''
    import random
    file_name = 'answers' + str(random.randint(1, 1000)) + '.txt'
    answer_file = open(file_name, 'w')
    for answer in range(0, 21):
        answer_file.write(str(random.choice(['A', 'B', 'C', 'D'])) + '\n')
    return file_name


def grade_answers(answer_key, answer_file):
    '''open answer file and write to list
    assign key file to list
    compare indexes between each lists
    update score by 1 if correct'''
    answers = []
    file = open(answer_file, 'r')
    for answer in file:
        answers.append(answer.rstrip('\n'))
    file.close()

    print(answers)

    keys = answer_key

    score = 0
    for i in range(len(keys)):
        if answers[i] == keys[i]:
            score += 1
    return score


def scoring(score):
    if score >= 15:
        result = 'pass'
    else:
        result = 'fail'
    return result


def main():
    try:
        answer_key = create_answer_key()
        print("answer key is", answer_key)
    except Exception:
        print("Error generating answer key")

    try:
        file_name = create_random_answers()
        print("file name is",file_name)
    except Exception:
        print("Error creating random student file")

    try:
        score = grade_answers(answer_key, file_name)
        print("score is", score)
    except Exception:
        print("Score could not be calculated")

    try:
        pass_or_fail = scoring(score)
        print("This student", pass_or_fail, 'ed.')
    except Exception:
        print("Error determining pass or fail")

    finally:
        print("Thanks for coming to the DMV, please take a number!")


main()









