# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Import libraries
import numpy as np
import pandas as pd
from datetime import date

#Create empty lists to organise data
ITEMS_OR_RESOURCES = []
PRICES = []
DATES = []
EXPENSE_GROUPS = []

# Function to add expenses to lists and structure input data 

def add_expense(item_or_resource, price, date, expense_group):
    """
    Adds all aspects of each expense to a list. 
    Stores the data input by the for each part of an individual expense. 
    """
    ITEMS_OR_RESOURCES.append(item_or_resource)
    PRICES.append(formatted_price)
    DATES.append(date)
    EXPENSE_GROUPS.append(expense_group)


# Output and processing program
# This will be the number input by the user: 
choice = 1
while choice != 0:
    # Create and display input choice list to users
    print('Welcome to Athleticoin, \n Manage your sports expenses here! \n')
    print('1. Create Equipment Expense')
    print('2. Create Coaching Expense')
    print('3. Create Transport Expense')
    print('4. Create Clothing or Footwear Expense')
    print('5. Allocate to savings')
    print('6. Save Expenses and Show My Report')
    print('0. Exit and Clear\n')
    choice = int(input('Please choose an action: \n'))

    print('\n')
    # Check input choice from the user 
    if choice == 0:
        print('You are exiting the program')
        break
    elif choice == 1:
        print('Add Equipment Cost')
        expense_group = 'EQUIPMENT'
    elif choice == 2:
        print('Add Coaching Cost')
        expense_group = 'COACHING'
    elif choice == 3: 
        print('Add Transport Cost')
        expense_group = 'TRANSPORT'
    elif choice == 4: 
        print('Add Clothing or Footwear Cost')
        expense_group = 'CLOTHING'
    elif choice == 5:
        print('Allocate to Savings Fund')
        expense_group = 'SAVINGS'
    elif choice == 6:
        # Show Data Frame - MAKE THIS INTO A FUNCTION TO CALL HERE ??
        expense_report = pd.DataFrame()
        expense_report['ITEMS_OR_RESOURCES'] = ITEMS_OR_RESOURCES
        expense_report['PRICES'] = PRICES
        expense_report['DATES'] = DATES
        expense_report['EXPENSE_GROUPS'] = EXPENSE_GROUPS
        # Save the report?
        expense_report.to_csv('report.csv')
        # Show Report??
        print(expense_report)
    else:
        print('You chose an invalid character.')
        print('Please choose a number between 0 and 6\n')


    # Create inputs for user to add price and expense name
    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        item_or_resource = input(f'Enter the name of this expense under the {expense_group} group \n')
        price = input('Enter the price of this expense: \n')
        formatted_price = round(float(price), 2)
        date = date.today()
        add_expense(item_or_resource, price, date, expense_group)


    # Create else statement for user to allocate some savings to the 
    # expense tracker???
    # Create a new variable for savings ? 
        
