
#_-_-_-_-_-_-_-_-_-_-_
#prints the current time.
from datetime import datetime

def print_time():
    print(datetime.now())

print("Hello World! Here is the current time.")
print_time()  ##DONT FORGET THE PARENTHESIS AFTER CALLING THE FUNCTION
#_-_-_-_-_-_-_-_-_-_-_

#does the same as print_time but allows the user to passs the message to dateime.now instead of needing a print statement each time.
from datetime import datetime

def print_time_messege(message):
    """This function prints a message along with the current date and time.""" #This is a docstring. It is largely ignored by the program. Good for documentation.
    print(message)
    print(datetime.now())
    
print_time_messege("Hello World! Here is the current time.")  ##Message in the parentesis is passed to the function, then is printed
#_-_-_-_-_-_-_-_-_-_-_

def get_initial(name = " ", capitalize = True):
    """This function returns the first letter of the name"""
    if capitalize:
        initiial = name[0:1].capitalize()
    else:     
        my_initial = name[0:1]
    return my_initial

def main():
    """Collects the name, then prints the first name"""
    my_name = input('What  is your first name?: ')
    my_initial = get_initial(my_name)
    print(f'Your first initial is {my_initial}')

main() #runs the main function


    
#_-_-_-_-_-_-_-_-_-_-_

