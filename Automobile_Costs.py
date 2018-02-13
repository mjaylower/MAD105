# Write a program that asks the user to enter the monthly costs for the
# following expenses incurred from operating his or her automobile: loan payment, insurance, gas, and maintenance.
# The program should then display the total monthly cost of these expenses,
# and the total annual cost of these expenses.

# explain what the program will do
def main():
    print('This program will determine the monthly and annual cost of operating your automobile.')
# run the monthly input function to get total monthly cost and pass parameter and run annual cost function
    monthly_input()

# gather user input for cost associated with automobile
def monthly_input():
    loan = float(input('How much is your monthly loan payment: ')) # get loan payment
    insurance = float(input('How much is your monthly insurance payment: ')) # get insurance payment
    gas = float(input('How much do you spend on gas per month: ')) # get gas payments
    maintenance = float(input('How much do you spend on maintenance per month: ')) # get maintenance payments
    monthly_payment = loan + insurance + gas + maintenance # add all payments together for monthly total

    print('You are spending on average $', format(monthly_payment, ',.2f'), 'per month.' )

    annual_cost(monthly_payment) # pass the monthly total parameter to the annual cost function

def annual_cost(monthly):
    annual = monthly * 12 # multiple monthly total by 12 to obtain annual cost

    print('Your annual automobile expenses will be approximately: $', format(annual, ',.2f'))

main()
