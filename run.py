# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Import libraries
from datetime import date
import re
import numpy as np
import pandas as pd

# Create empty lists to organise data
ITEMS_OR_RESOURCES = []
PRICES = []
DATES = []
EXPENSE_GROUPS = []

# Global Variables
date = date.today()
choice = -1
item_or_resource = ""
price = ""
expense_group = ""
formatted_price = ""


# Function to add expenses to lists and structure input data 
def add_expense(item_or_resource, price, date, expense_group):
    """
    Adds all aspects of each expense to a list.
    Stores the data input by the for each part of an individual expense.
    """
    ITEMS_OR_RESOURCES.append(item_or_resource)
    PRICES.append(price)
    DATES.append(date)
    EXPENSE_GROUPS.append(expense_group)


def show_report():
    """
    Function to display expenses input by user
    Shows as a Pandas data frame
    """
    expense_report = pd.DataFrame()
    expense_report['ITEMS_OR_RESOURCES'] = ITEMS_OR_RESOURCES
    expense_report['PRICES'] = PRICES
    expense_report['+ VAT'] = expense_report['PRICES'] * 1.2
    expense_report['+ VAT'] = np.round(expense_report['+ VAT'], decimals=2)
    expense_report['DATES'] = DATES
    expense_report['EXPENSE_GROUPS'] = EXPENSE_GROUPS
    expense_report.loc['TOTAL', 'PRICES'] = expense_report['PRICES'].sum()
    expense_report.loc['TOTAL', '+ VAT'] = expense_report['+ VAT'].sum()
    expense_report = expense_report.fillna('')
    # Save the report
    expense_report.to_csv('report.csv')
    # Show Report
    print(expense_report)
    print()


def show_intro():
    """
    Shows introduction message and instructions
    to user
    """
    print()
    print('Welcome to Athleticoin!')
    print('An easy way to manage your sports expenses\n')
    print('There are multiple categories to add expenses to')
    print('Your saved report provides an overview of all your expenses')
    print('You will be provided with a total and added VAT on saving a report')
    print('NOTE: all numbers input will be rounded to 2 decimal places')
    print('Press a number related to one of the options below to get started!')
    print()


show_intro()


def input_choices():
    """
    Shows input choices to the user 
    """
    print('1. Create Equipment Expense')
    print('2. Create Coaching Expense')
    print('3. Create Transport Expense')
    print('4. Create Clothing or Footwear Expense')
    print('5. Allocate funds to team savings')
    print('6. Save Expenses and Show My Report')
    print('0. Exit and Clear\n')
    global choice
    choice = input('Please choose an action: \n')
    print()


def input_expense_price():
    """
    User inputs price of expense after name given
    Only accepts numbers as input
    """
    price = input('Enter the price of this expense: \n')
    if not re.search(r'^[-+]?[0-9]*\.?[0-9]+$', price):
        print(
            'Invalid input. Please enter a number')
        input_expense_price()
    else:
        formatted_price = round(float(price), 2)
        add_expense(
            item_or_resource, formatted_price, date, expense_group)
        input_choices()


def input_expense_name():
    """
    User inputs name of expense under chosen group
    Requires input to continue to price input
    """
    while True:
        global item_or_resource
        item_or_resource = input(
                f'Enter the name of this {expense_group} expense\n')
        if item_or_resource == "":
            print('Please assign an expense name!')
            input_expense_name()
        else:
            input_expense_price()
            break


def input_savings_number():
    """
    Prompts user to enter value of savings
    Only takes integers as inputs 
    """
    while True:
        # global price
        price = input('Enter the amount you would like to allocate\n')
        if not re.search(r'^[-+]?[0-9]*\.?[0-9]+$', price):
            print(
                'Invalid input. Please enter a number to add to savings'
                )
            input_savings_number()
        else:
            formatted_price = round(float(price), 2)
            add_expense(
                item_or_resource, formatted_price, date, expense_group)
        break


def input_savings_reason():
    """
    Prompts user to input reason for allocating funds to savings
    Requires input to continue
    """
    # if choice == '5':
    # while True:
    global item_or_resource
    item_or_resource = input(
        'Enter the reason for allocating funds to savings\n')
    if item_or_resource == "":
        print('Please assign an expense name')
        input_savings_reason()
    else:
        input_savings_number()
  

# MAKE THIS A FUNCTION??
# Output and processing program
# while True:  # choice != 0:  # Put this while loop in a function??
    # Create and display input choice list to users
    # show_intro()
input_choices()
choice = input('Please choose an action: \n')
print()

# Check input choice from the user - make this a function to call in main?
while True:
    if choice == '0':
        print('You are exiting the program')
        break
    elif choice == '1':
        # print('Add Equipment Cost')
        expense_group = 'EQUIPMENT'
        input_expense_name()
    elif choice == '2':
        print('Add Coaching Cost')
        expense_group = 'COACHING'
        input_expense_name()
    elif choice == '3': 
        print('Add Transport Cost')
        expense_group = 'TRANSPORT'
        input_expense_name()
    elif choice == '4':
        print('Add Clothing or Footwear Cost')
        expense_group = 'CLOTHING'
        input_expense_name()
    elif choice == '5':
        print('Allocate to Savings Fund')
        input_savings_reason()
        expense_group = 'SAVINGS'
    elif choice == '6':
    # Show Expenses in Data Frame 
        show_report()
        break
    elif not re.search(r'^[-+]?[0-6]', choice):
        print('Invalid input, please enter a value from the options!')
    # input_choices()  # CHANGE THIS TO SHOW OPTIONS WITH NO INTRO??
    else:
        print('You chose an invalid number.')
        print('Please choose a number option between 0 and 6\n')
        break
    # input_choices()  # CHANGE THIS TO SHOW OPTIONS WITH NO INTRO??


# Create inputs for user to add price and expense name
    
    """
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
        item_or_resource = input(
            f'Enter the name of this {expense_group} expense\n')
        if item_or_resource == "":
            print('Please assign an expense name')
        price = input('Enter the price of this expense: \n')
        if not re.search(r'^[-+]?[0-9]*\.?[0-9]+$', price):
            print(
                'Invalid input. Please enter a number')
            # price = input('Enter the price of this expense: \n')
        else:
            formatted_price = round(float(price), 2)
            add_expense(
                item_or_resource, formatted_price, date, expense_group)



    if choice == '5':
        while True:
            item_or_resource = input(
                f'Enter the reason for allocating funds to {expense_group}\n')
            if item_or_resource == "":
                print('Please assign an expense name')
                continue
            price = input('Enter the amount you would like to allocate\n')
            if not re.search(r'^[-+]?[0-9]*\.?[0-9]+$', price):
                print(
                    'Invalid input. Please enter an amount to add to savings'
                )
            # price = input('Enter the amo)
                break
            else:
                formatted_price = round(float(price), 2)
                add_expense(
                    item_or_resource, formatted_price, date, expense_group)
                break
"""
