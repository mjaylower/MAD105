import pickle

# GLOBAL CONSTANTS FOR MENU OPTIONS
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT_AND_SAVE = 5


def main():
    try:
        input_file = open('name_and_email.dat', 'rb')  # TRIES TO OPEN DATA FILE WITH 'RB' SO IT CAN PICKLE
        name_and_email = pickle.load(input_file)  # DATA FOUND ON FILE WILL BE MAPPED TO VARIABLE
        # print(name_and_email)  # USED TO TEST CONTENT OF FILE TO ENSURE READING DATA CORRECTLY
    except (FileNotFoundError, IOError):  # IF EITHER ERROR OCCURS, FOLLOWING WILL TAKE PLACE
        print('File Not Found, Please Add Data To Create New File')  # SAYS NO FILE FOUND, NEED TO CREATE AND SAVE WITHIN PROGRAM
        name_and_email = {}  # CREATES AN EMPTY DICTIONARY SINCE ONE DOESN'T EXIST YET BASED ON ERROR OCCURRENCE

    choice = 0  # INITIALIZES VARIABLE FOR MENU OPTIONS

    while choice != QUIT_AND_SAVE:  # INITIALIZES THE WHILE LOOP SO LONG AS QUIT_AND_SAVE (5) ISN'T SELECTED
        choice = get_menu_choice()  # RUN THE 'GET_MENU_CHOICE' FUNCTION AND RETURN 'ANSWER'

        if choice == LOOK_UP:  # IF 1 IS SELECTED, RUN THE 'LOOK_UP' FUNCTION
            look_up(name_and_email)
        elif choice == ADD:  # IF 2 IS SELECTED, RUN THE 'ADD' FUNCTION
            add(name_and_email)
        elif choice == CHANGE:  # IF 3 IS SELECTED, RUN THE 'CHANGE' FUNCTION
            change(name_and_email)
        elif choice == DELETE:  # IF 4 IS SELECTED, RUN THE 'DELETE' FUNCTION
            delete(name_and_email)
        elif choice == QUIT_AND_SAVE:  # IF 5 IS SELECTED, RUN THE 'QUIT_AND_SAVE' FUNCTION - PROGRAM ENDS
            quit_and_save(name_and_email)


# OPEN MENU OPTIONS
def get_menu_choice():

    print('')
    print('NAMES | EMAILS')
    print('---------------------------')
    print('1: LOOK UP EMAIL BY NAME')
    print('2: ADD NEW NAME & EMAIL')
    print('3: CHANGE EXISTING EMAIL')
    print('4: DELETE NAME & EMAIL')
    print('5: QUIT & SAVE')
    print('')

    answer = int(input('MENU SELECTION: '))  # ASK USER FOR MENU SELECTION

    while answer < 1 or answer > 5:  # VALIDATE MENU SELECTION
        answer = int(input('Enter a valid option: '))

    return answer  # RETURN INT VALUE SELECTION TO MAIN FUNCTION


# LOOK UP NAME (KEY) IN THE 'NAME_AND_EMAIL' DICTIONARY AND DISPLAY EMAIL (VALUE), IF FOUND
def look_up(name_and_email):
    # get a name
    name = input('Name To Search: ')  # ASK USER FOR NAME TO SEARCH

    print(name_and_email.get(name, name + ' Was Not Found'))  # PRINT EMAIL (VALUE) OF THE NAME (KEY) ENTERED, IF FOUND


# ADD NAME AND EMAIL TO 'NAME_AND_EMAIL' DICTIONARY
def add(name_and_email):
    name = input('Name To Add: ')  # ASK USER TO ENTER A NAME (WILL BE THE KEY)

    if name not in name_and_email:  # IF NAME DOESN'T EXIST, ADD NEW KEY-VALUE PAIR TO NAME_AND_EMAIL DICTIONARY
        email = input(name + "'s Email: ")  # ASK USER TO ENTER AN EMAIL (WILL BE THE VALUE)
        name_and_email[name] = email
        print(name + ' has been added to your database')

    else:
        print(name + ' already exists')
        print('Please select the "CHANGE" option to make an update to ' + name + "'s email.")
        print('OR, please specify further which ' + name + ' you\'re referring to.')


# CHANGE EMAIL OF EXISTING NAME FROM NAME_AND_EMAIL DICTIONARY
def change(name_and_email):

    name = input('Name To Update: ')  # ASK USER FOR NAME TO UPDATE
    if name in name_and_email:  # IF NAME EXIST IN DICTIONARY, ASK USER FOR NEW EMAIL
        email = input('Enter ' + name + "'s new email: ")
        print('Thank you, ' + name + "'s email has been updated.")

        # UPDATE EMAIL IN THE KEY-VALUE PAIR IN NAME_AND_EMAIL DICTIONARY
        name_and_email[name] = email

    else:
        print(name + ' Was Not Found')
        print('Please select the "ADD" option to add ' + name + ' to the database.')


# DELETE NAME AND EMAIL FROM DICTIONARY
def delete(name_and_email):

    name = input('Name To Delete: ')  # ASK USER FOR NAME TO DELETE

    if name in name_and_email:  # IF NAME EXIST IN DICTIONARY, DELETE KEY-VALUE PAIR
        del name_and_email[name]
        print(name + ' has been deleted.')
    else:
        print(name + ' Was Not Found')
        print('Looks like you don\'t need to delete ' + name + ' after all!')


# SAVE DATA TO FILE AND EXIT PROGRAM
def quit_and_save(name_and_email):
    print('Sorry to see you go, but rest assured')
    print('your data has been saved.')
    print('Good Bye')

    save_file = open('name_and_email.dat', 'wb')  # OPEN FILE AND ENABLE BINARY WRITING 'WB'
    pickle.dump(name_and_email, save_file)  # DUMP NEW DATA FROM DICTIONARY INTO FILE
    save_file.close()  # CLOSE FILE


# EXECUTE PROGRAM
main()
