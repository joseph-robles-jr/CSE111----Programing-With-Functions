from datetime import datetime

def bmi(weight, height):
	'''Finds bmi from weight and height'''
	return (10000 * weight) / (height ** 2)
  
def bmr_women(weight, height, age):
	'''Finds bmr for women from weight, height, and age'''
	return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

def bmr_men(weight, height, age):
	'''Finds bmr for men from weight, height, and age'''
	return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)



def compute_age(birth_str):
	"""Compute and return a person's age in years.
	Parameter birth_str: a person's birthdate stored
		as a string in this format: YYYY-MM-DD
	Return: a person's age in years.
	"""
	# Convert a person's birthdate from a string
	# to a date object.
	birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
	today = datetime.now()

	# Compute the difference between today and the
	# person's birthdate in years.
	years = today.year - birthdate.year
	return years
    
    
def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kg = pounds * 0.45359237
    return kg

    
def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    #Converts inches to centimeters (1 in = 2.54 cm).
    cm = inches * 2.54
    return cm
    
    
def main():
	'''Asks for the gender, birdate, weigth and height of the person. 
	Then converts the weight into kg and the height into cm. 
	Calls previous functions to calc bmi and bmr for men and women'''
	gender = input("What is your gender? (M/F) ").lower()
	birthdate = (input("What is your date of birth? (YYYY-MM-DD) "))
	weight_lbs = float(input("What is your weight in pounds? "))
	height_inches = float(input("What is your height in inches? "))
        
	weight_kg = kg_from_lb(weight_lbs)
	height_cm = cm_from_in(height_inches)
	age = compute_age(birthdate)
    
    if gender == "f" and age > 35:
        age = age - 10
    
    if gender == "f" and weight_kg > 80:
        weight_kg = 80
    
    
    if gender == 'f':
		bmr = bmr_women(weight_kg, height_cm, age)
	else:
		bmr = bmr_men(weight_kg, height_cm, age)
      
	persons_bmi = bmi(weight_kg, height_cm)
  
	print(f'Age (years): {age}')
	print(f'Weight (kg): {weight_kg:.2f}')
	print(f'Height (cm): {height_cm:.2f}')
	print(f'Body mass index: {persons_bmi:.2f}')
	print(f'Basal metabolic rate (kcal/day): {bmr:.2f}')
    
main()
    
   
    
    
    
    
    
    