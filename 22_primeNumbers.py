"""
	Program receives user input
	and tells the user if the
	number entered is a Prime
	or not.
"""

def check_prime(number):
    if (number == 1):
        prime = False ;
    else:
        prime = True ;
    
    for i in range(1, number):
        if (i == 1):
            continue ;
        if (number % i == 0):
            prime = False ;
            break ;
    
    if (prime == True):
        print("\nIt's a prime number.\n") ;
    else:
        print("\nIt's not a prime number.\n") ;


number = int(input("\nEnter a number: ")) ;


check_prime(number) ;

