"""
    Program works as a randomized
    Password Generator by first
    receiving the number of Letters,
    Symbols, and Numbers the user would
    like to have in their new password;
    appending each to a new list; randomly 
    removing them from the list, and linking 
    them together to form a new password.
"""


import random

seed_num = random.randint(1, 1000) ;

random.seed(seed_num) ;

letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 
            'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z', 'A', 'B', 'C', 'D', 
            'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 
            'Q', 'R', 'S', 'T', 'U', 'V', 
            'W', 'X', 'Y', 'Z' ]

symbols = [ '!', '#', '$', '%', '&', '(', ')', '*', '+' ]

numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]


PASSWORD = [] ;


print("\n\n\t\t *** RANDOM PASSWORD GENERATOR *** \n\n") ;

numLetters= int( input(" Enter the number of Letters you want in your password: ") ) ;
print("\n") ;

for x in range(numLetters):
    PASSWORD.append( random.choice(letters) ) ;


numSymbols = int( input(" Enter the number of Symbols you want in your password: ") ) ;
print("\n") ;

for y in range(numSymbols):
    PASSWORD.append( random.choice(symbols) ) ;


numNumbers = int( input(" Enter the amount of Numbers you want in your password: ") ) ;
print("\n") ;

for z in range(numNumbers):
    PASSWORD.append( random.choice(numbers) ) ;



new_password = "" ;

for info in range( len(PASSWORD) ):
    random.shuffle(PASSWORD) ;
    temp = random.choice(PASSWORD) ;
    new_password += temp ;
    PASSWORD.remove(temp) ;


print(f" ENJOY YOUR NEW PASSWORD:       {new_password} \n\n") ;

