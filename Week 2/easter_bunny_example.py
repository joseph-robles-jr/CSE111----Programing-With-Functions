months = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
first_names = ['Lucky','Candy','Spanky','Thumpy','Pinky','Beans','Nibble','Poppy','Flo','Sweety','Coco','Peeps','Toothy','Trixie','Hopper','Sparky','Loco','Pepe','Bubbles','Fluffy','Chompy','Flower','Stuffy','Paws','Daffy','Dizzy']
last_names = ['Snuggles','Happy Feet','McFuzzy','Sprinkleton','Lollipopper','Cotton Tail','Baby Carrot','MacDoodle','Hop-To-It','McFluffenstein','Plastic Eggs','Sweet Bottom']

def main():
    """  This function gathers the needed information to create your easter bunny name
        by asking for your birth month and name.
        The program uses your first name initial to map to the first names list
        The program uses your birth month to map to the last names list.
        The program then constructs your easter bunny name using this information."""
    
    first_name = input('What is your first name?: ')
    birth_month = input('What is the month of your birth: ').upper()
    
    initial = get_initial(first_name).upper()
    bunny_first_name = get_bunny_first_name(initial)
    
    month_number = get_month_number(birth_month)
    bunny_last_name = get_bunny_last_name(month_number)
    
    print(f'your Easter Bunny name is {bunny_first_name} {bunny_last_name}')
    
    
def get_initial(first_name):
    return first_name[0:1]

def get_bunny_first_name(initial):
    index = ord(initial) - 65 #Gives ascii value of letter. subracting 65 makes 1=A 2=B 3=C etc....
    return first_names[index]

def get_month_number(month):
    return months.index(month) #finds month in list, returns the associated number

def get_bunny_last_name(month_number):
    return last_names[month_number]

main()
