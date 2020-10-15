# Saeed has changed
#Saeed was here again


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
from src.data.db import people_dict, drinks_dict

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
