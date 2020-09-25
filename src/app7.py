# Author: Kathryn Holloway
# Version: 5.0 16/09/2020
# Changing user input, using docopt instead of sys.argv
# Adding in classes in line with OOP learning
# Add print order using order class
# DATA ENCODING: taking data in from csv  

# NOTE:
# Cannot handle person duplicates; makes preferences a nested dict to handle?
# NOTE: put the data functions into a class 

#NOTE: I made these changes on test_branch
"""Usage:
app.py (get-people | get-drinks)
app.py menu
app.py -h | --help

"""
# NOTE: doesn't handle multiple arguments
#install requirements
# py -m pip install -r requirements.txt for docopt
# py -m pip freeze > requirements.txt to make requirements file


from docopt import docopt
import src.output.tables as t
import src.classes.order as order #NOTE: added 'as order' to fix referencing further down 
import src.menu.cli as cli
from src.persistence.data_persistence import people_dict, drinks_dict

# Define the data

# Dictionaries 
# people_dict = {1:"Emma",2:"Olivia",3:"Ava",4:"Isabella",5:"Sophia",6:"Charlotte",7:"Mia",8:"Kate"}
# drinks_dict = {1:"Tea", 2:"Coffee",3:"Water",4:"Juice",5:"Beer",6:"Wine"}

# preferences_dict = {"Kate":"Tea", "Emma":"Coffee", "Ava":"Juice", "Mia":"Water"}

# Dictionary of valid arguments and their corresponding table 'header' and data
# VALID_ARGS = {"get-people":['people',people_dict],"get-drinks":['drinks',drinks_dict]}


# This is the root of the programs controls

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.1rc2')
    # print(arguments)

    #parse the arguments
    if arguments.get('get-people') == True:
        t.print_table(t.generate_table('people',people_dict))
    if arguments.get('get-drinks') == True:
        t.print_table(t.generate_table('drinks',drinks_dict))
    elif arguments.get('menu') == True:
        cli.get_user_input()
    else:
        # Docopt handles no input and bad input
        pass
