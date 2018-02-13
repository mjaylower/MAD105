# set up global variable
total_calories = 0


def main():
    # locally define the global variable
    global total_calories

    # run the remaining 3 functions
    fat()
    carbohydrate()
    protein()

    # print the total calories accumulated from the previous 3 functions
    print('You consumed', format(total_calories, ','), 'calories today.')


def fat():
    # locally define the global variable
    global total_calories

    # ask for grams of fat and calculate fat calories
    fat_grams = int(input('How many grams of fat today: '))
    fat_calories = fat_grams * 9

    # add fat calories to the global variable
    total_calories = total_calories + fat_calories

    # display total calories from fat
    print('You ate', format(fat_calories, ','), 'calories from fat.')


def carbohydrate():
    # locally define the global variable
    global total_calories

    # ask for grams of carbohydrates and calculate carbohydrate calories
    carbohydrate_grams = int(input('How many grams of carbohydrates today: '))
    carbohydrate_calories = carbohydrate_grams * 4

    # add carbohydrate calories to the global variable
    total_calories += carbohydrate_calories

    # display total calories from carbohydrates
    print('You ate', format(carbohydrate_calories, ','), 'calories from carbohydrates.')


def protein():
    # locally define the global variable
    global total_calories

    # ask for grams of protein and calculate protein calories
    protein_grams = int(input('How many grams of protein today: '))
    protein_calories = protein_grams * 4

    # add protein calories to the global variable
    total_calories += protein_calories

    # display total calories from proteins
    print('You ate', format(protein_calories, ','), 'calories from protein.')


# run the main function
main()
