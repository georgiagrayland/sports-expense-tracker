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