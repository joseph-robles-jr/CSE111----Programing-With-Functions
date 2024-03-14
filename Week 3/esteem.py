import time

def pause():
  print()
  time.sleep(1.5)


def letter_to_number(letter):
	"""Converts "letter" A --> 0, a --> 1, d --> 2, D --> 3"""
    
	#strong agree
	if letter == 'A':
		output = 3
	#agree
	elif letter == 'a':
		output = 2
    
	#Disagree
	elif letter == 'd':
		output = 1
	
	#strong Disagree
	elif letter == 'D':
		output = 0
    
	return output

def invert(zero_to_3):
    
    """Inverts inputs between 0 and 3"""
    
    if zero_to_3 == 0:
        output = 3
    elif zero_to_3 == 1:
        output = 2
    elif zero_to_3 == 2:
        output = 1
    elif zero_to_3 == 3:
        output = 0
    return output
 
  
def main():
    
    print('This program is an implementation of the Rosenberg	Self-Esteem Scale. This program will show you ten	statements that you could possibly apply to yourself.Please rate how much you agree with each of thestatements by responding with one of these four letters: ')
    pause()
    print('D means you strongly disagree with the statement.')
    pause()
    print('d means you disagree with the statement.')
    pause()
    print('a means you agree with the statement.')
    pause()
    print('A means you strongly agree with the statement.')
    pause()
  
    worth_p = input('I feel that I am a person of worth, at least on an equal plane with others. ')
    qualities_p = input('I feel that I have a number of good qualities. ')
    failure_f = input('All in all, I am inclined to feel that I am a failure. ')
    people_p = input('I am able to do things as well as most other people. ')
    proud_f = input('I feel I do not have much to be proud of. ')
    attitude_p = input('I take a positive attitude toward myself. ')
    satisfied_p = input('On the whole, I am satisfied with myself. ')
    respect_f = input('I wish I could have more respect for myself. ')
    useless_f = input('I certainly feel useless at times. ')
    good_f = input('At times I think I am no good at all. ')
  
    w_num = letter_to_number(worth_p)
    q_num = letter_to_number(qualities_p)
    f_num = letter_to_number(failure_f)
    pe_num = letter_to_number(people_p)
    pr_num = letter_to_number(proud_f)
    a_num = invert(letter_to_number(attitude_p))
    s_num = invert(letter_to_number(satisfied_p))
    r_num = invert(letter_to_number(respect_f))
    u_num = invert(letter_to_number(useless_f))
    g_num = invert(letter_to_number(good_f))
  
    sum_of_values = w_num + q_num + f_num + pe_num + pr_num + a_num + s_num + r_num + u_num + g_num  
  
    print(f'Your score is {sum_of_values}')
    print('A score below 15 may indicate problematic low self-esteem')
  
  
  
main()