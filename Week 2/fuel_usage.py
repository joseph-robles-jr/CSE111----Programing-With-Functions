def main():
    # Get an odometer value in U.S. miles from the user.
    odometer_init = int(input("What is your innitial odometer reading in U.S. Miles?: "))

    # Get another odometer value in U.S. miles from the user.
    odometer_sec = int(input("What is your second odometer reading in U.S. Miles?: "))
    # Get a fuel amount in U.S. gallons from the user.
    fuel_used=float(input("How much fuel has been used in U.S. Gallons?: "))
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(odometer_init, odometer_sec, fuel_used)
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Display the results for the user to see.
    print(f'Your MPG is {mpg} and your Lp100k is {lp100k}. ')


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    mpg = (end - start) /gallons
    

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    
    mpg = (end_miles - start_miles) / amount_gallons
    
    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    lp100k  = 235.215 / mpg
    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k  = 235.215 / mpg
    
    return lp100k


# Call the main function so that
# this program will start executing.
main()