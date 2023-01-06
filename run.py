# Write your code to expect a terminal of 80 characters wide and 24 rows high

#Import libraries
import numpy as np
import pandas as pd
from datetime import date

#Create empty lists to organise data
ITEMS_OR_RESOURCES = []
PRICES = []
DATES = []
EXPENSE_GROUPS = []

#Function to add expenses to lists and structure input data 

def add_expense(item_or_resource, price, date, expense_group):
    """
    Adds all aspects of each expense to a list. 
    Stores the data input by the for each part of an individual expense. 
    """
    ITEMS_OR_RESOURCES.append(item_or_resource)
    PRICES.append(price)
    DATES.append(date)
    EXPENSE_GROUPS.append(expense_group)


#Output and processing program
choice = -1 #This will be the number input by the user 
while choice != 0:
    #Create and display input choice list to users
    print('Welcome to Athleticoin, \n Manage your sports expenses here! \n')
    print('1. Create Equipment Expense')
    print('2. Create Coaching Expense')
    print('3. Create Transport Expense')
    print('4. Create Clothing or Footwear Expense')
    print('5. Allocate to savings')
    print('6. Save Expenses and Show All')
    print('0. Exit and Clear')