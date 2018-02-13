# Write a program that asks a user to enter five test scores.
# You will need to create five variables to hold these scores.

# The purpose of this assignment is to get practice passing information between functions,
# this is not a good example of the way programs are really written,
# but it will help you to understand how to pass parameters.


def main():
    print('This program will determine the letter grade based on your 5 test scores.')
    print('Please enter the 5 test scores below.')

    # get user input for each test score
    score1 = int(input('Test Score 1: '))
    score2 = int(input('Test Score 2: '))
    score3 = int(input('Test Score 3: '))
    score4 = int(input('Test Score 4: '))
    score5 = int(input('Test Score 5: '))

    # function 1
    average = cal_average(score1, score2, score3, score4, score5)
    print('Average Score:', average)

    # function 2
    final_grade = determine_grade(average)
    print('Final Grade:', final_grade)


# calculate the average of the 5 test scores via passed arguments
def cal_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average  # return the average score to be passed and determine the letter grade


# using the passed average, determine the letter grade
def determine_grade(grade):
    if grade >= 90:
        return 'A'  # return A if score is greater than or equal to 90
    elif 89 >= grade >= 80:
        return 'B'  # return B if score is between 80-89
    elif 79 >= grade >= 70:
        return 'C'  # return C if score if between 70-79
    elif 69 >= grade >= 60:
        return 'D'  # return D if score is between 60-69
    else:
        return 'F'  # return F is score is less than 60


main()
