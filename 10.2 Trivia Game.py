class Question:

    # set the initializer for class question with all attributes
    # set all the objects to private
    def __init__(self, question, a1, a2, a3, a4, answer):
        self.__question = question
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__answer = answer

    def set_question(self, question):
        self.__question = question

    def set_a1(self, a1):
        self.__a1 = a1

    def set_a2(self, a2):
        self.__a2 = a2

    def set_a3(self, a3):
        self.__a3 = a3

    def set_a4(self, a4):
        self.__a4 = a4

    def set_answer(self, answer):
        self.__answer = answer

    # methods to return the arguments that have been passed
    def get_question(self):
        return self.__question

    def get_a1(self):
        return self.__a1

    def get_a2(self):
        return self.__a2

    def get_a3(self):
        return self.__a3

    def get_a4(self):
        return self.__a4

    def get_answer(self):
        return self.__answer


def main():

    # establish the list of 10 questions to be asked
    q0 = Question('What is Joey\'s profession?', 'A) Sandwich Shop Owner', 'B) Actor', 'C) Massage Therapist',
                  'D) Unemployed', 'B')
    q1 = Question('What is the name of Ross and Rachel\'s baby?', 'A) Emily', 'B) Julie', 'C) Emma',
                  'D) Monica', 'C')
    q2 = Question('What is the name of Ross\'s monkey:', 'A) Marcel', 'B) Marcus', 'C) Mark',
                  'D) Ross never had a monkey', 'A')
    q3 = Question('How many categories for towels does Monica have?', 'A) 4', 'B) 11', 'C) 7', 'D) 15', 'B')
    q4 = Question('What high school did Ross, Monica and Rachel attend?', 'A) JFK HS', 'B) Lincoln HS',
                  'C) State Public Schools', 'D) St. Mary HS', 'B')
    q5 = Question('What country does Chandler pretend to move to?', 'A) Canada', 'B) Brazil', 'C) Yemen',
                  'D) London', 'C')
    q6 = Question('What fruit is Ross allergic to?', 'A) Orange', 'B) Strawberry', 'C) Kiwi', 'D) Mango', 'C')
    q7 = Question('What instrument does Phoebe play?', 'A) Piano', 'B) Flute', 'C) Guitar',
                  'D) She only sings', 'C')
    q8 = Question('Where do Phoebe and Mike get married?', 'A) Church', 'B) Street', 'C) Central Perk',
                  'D) Court House', 'B')
    q9 = Question('What color is the couch at Central Perk', 'A) Green', 'B) Red', 'C) Purple', 'D) Orange', 'D')

    # initialize score counter for both players
    player1 = 0
    player2 = 0

    # create the two sets of questions, 1 for each player
    question_set_1 = [q1, q3, q5, q7, q9]
    question_set_2 = [q0, q2, q4, q6, q8]

    # Ask player 1 each question from the list
    print('Player 1')
    print('--------')
    for query in question_set_1:  # for each element in the list, display options via class question
        print('\n')
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input('Please enter the letter of the correct answer: ')  # ask user for answer via letter selection
        if guess.upper() == query.get_answer():  # ensure letter given is now uppercase for comparision to get_answer
            print('You are correct!')  # express excitement
            player1 += 1  # if correct, add a point
            print('Total Score: ', player1)  # display current point total
        else:
            print('That is not correct :-( ')  # express disappointment
            print('Total Score: ', player1)  # display current point total
    print('\n')

    # ask player 2 each question for their list
    print('Player 2')
    print('--------')
    for query in question_set_2:  # for each element in the list, display options via class question
        print('\n')
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input('Please enter the letter of the correct answer: ')  # ask user for answer via letter selection
        if guess.upper() == query.get_answer():  # ensure letter given is now uppercase for comparision to get_answer
            print('You are correct!')  # express excitement
            player2 += 1  # if correct, add a point
            print('Total Score: ', player2)  # display current point total
        else:
            print('That is not correct :-( ')  # express disappointment
            print('Total Score: ', player2)  # if incorrect, display current point total
    print('\n')

    # compare the scores for each player to determine the winner
    print('THE RESULTS ARE IN!')
    print('-------------------')
    print('Player 1: ', player1)
    print('Player 2: ', player2)
    print('\n')
    if player1 > player2:
        print('Player 1 is the winner with', player1, 'points!')
    elif player2 > player1:
        print('Player 2 is the winner with', player2, 'points!')
    else:
        print('You TIED with', player1, 'points!')


# run the program
main()
