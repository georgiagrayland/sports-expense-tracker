# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Import libraries
from datetime import date
from colorama import Fore, Back, Style
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
    # Show Report to user 
    print(expense_report)
    print()


def show_intro():
    """
    Shows introduction message and instructions
    to user
    """
    print()
    print(Fore.GREEN + 'Welcome to Athleticoin!')
    print('An easy way to manage your sports expenses\n')
    print('There are multiple categories to add expenses to')
    print('Your saved report provides an overview of all your expenses')
    print('You will be provided with a total and added VAT on saving a report')
    print('NOTE: all numbers input will be rounded to 2 decimal places')
    print('Press a number related to one of the options below to get started!')
    print(Style.RESET_ALL)


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
    print(Fore.CYAN + '6. Save Expenses and Show My Report', end='')
    print(Style.RESET_ALL)
    print('0. Exit and Clear\n')
    try:
        global choice
        choice = int(input(Fore.YELLOW + 'Please choose an action: \n'))
        print(Style.RESET_ALL)
        if 0 <= choice <= 6:
            print()
        else:
            print(
                Fore.RED + "Please enter a number between 0-6", end='')
            print(Style.RESET_ALL)
            input_choices()
    except ValueError:
        print(Fore.RED + 'Invalid entry. Please choose from the options')
        print(Style.RESET_ALL)
        input_choices()


input_choices()


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
        print(
            Fore.MAGENTA + 'You added an expense.')
        print('What would you like to do next?')

        print(Style.RESET_ALL)
        input_choices()


def input_expense_name():
    """
    User inputs name of expense under chosen group
    Requires input to continue to price input
    """
    global item_or_resource
    item_or_resource = input(
            f'Enter the name of this {expense_group} expense\n')
    if item_or_resource == "":
        print('Please assign an expense name!')
        input_expense_name()
    else:
        input_expense_price()


def input_savings_number():
    """
    Prompts user to enter value of savings
    Only takes integers as inputs 
    """
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
        print('You allocated funds to savings.')
        print('What would you like to do next?\n')
        input_choices()


def input_savings_reason():
    """
    Prompts user to input reason for allocating funds to savings
    Requires input to continue
    """
    global item_or_resource
    item_or_resource = input(
        'Enter the reason for allocating funds to savings\n')
    if item_or_resource == "":
        print('Please assign an expense name')
        input_savings_reason()
    else:
        input_savings_number()
  

# Processing program
# Check input choice from the user
while True:
    if choice == 0:
        print('You are exiting the program')
        break
    elif choice == 1:
        print('Add Equipment Cost')
        expense_group = 'EQUIPMENT'
        input_expense_name()
    elif choice == 2:
        print('Add Coaching Cost')
        expense_group = 'COACHING'
        input_expense_name()
    elif choice == 3: 
        print('Add Transport Cost')
        expense_group = 'TRANSPORT'
        input_expense_name()
    elif choice == 4:
        print('Add Clothing or Footwear Cost')
        expense_group = 'CLOTHING'
        input_expense_name()
    elif choice == 5:
        print('Allocate to Savings Fund')
        expense_group = 'SAVINGS'
        input_savings_reason()
    elif choice == 6:
        show_report()
        break
    # else:
        # print(Fore.RED + 'You chose an invalid number.')
        # print('Please choose a number option between 0 and 6')
        # print(Style.RESET_ALL)
        # input_choices()