#importing a module.py
#module resides in a file in the working directory
#in this case: functions_passing_list.py


#import all functions, not recommended
#from functions_passing_list import *

#using an alias for the module
#from functions_passing_list as fpl

#Using an alias for the function
from functions_passing_list import books_available as ba,book_description as bd

#Stock functions
#from functions_passing_list import books_available,book_description

print("This is our 1st function: ")
ba('odyssey', 'illiad')
print("This is our 2nd function: ")
bd('homer')
