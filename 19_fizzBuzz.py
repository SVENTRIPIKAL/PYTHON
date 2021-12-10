"""
	Program runs through
	numbers from 1 to 100
	and prints 'Fizz' if 
	the number is divisible
	by {3}, 'Buzz' if divisible
	by {5}, 'FizzBuzz' if divisible
	by both, or the current number. 
"""


for number in range(1, 101):
    if ( (number % 3 == 0) and 
         (number % 5 == 0) ):
        print("FizzBuzz") ;
    
    elif (number % 3 == 0):
        print("Fizz") ;
    
    elif (number % 5 == 0):
        print("Buzz") ;
    
    else:
        print(number) ;

