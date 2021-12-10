"""
    Program receives a stringed two digit
    number via user-input, converts each
    digit to an integer-type, and prints
    the sum of both digits to the screen.
"""


two_digit_number = input("\nType a two digit number: ")

digit_1 = int(two_digit_number[0]) ; 

digit_2 = int(two_digit_number[1]) ;

print( digit_1 + digit_2 ) ;

