"""
	Program converts a user-input
	list of names {separated by commas}
	into a list and randomly selects a
	name from the list.
"""

import random


test_seed = int(input("Create a seed number: "))

random.seed(test_seed)


names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")



list_length = len(names) ;

index = (random.randint( 1, list_length )) - 1 ;

random_name = names[index] ;

print( f"{random_name} is going to buy the meal today!" ) ;

