""" 
    Simple program works as a Band Name
    Generator by concatenating user input.
"""
#1. Create Greeting
print( "\nTHIS IS A BAND NAME GENERATOR...\n\n" ) ;

#2. Ask user to enter city of origin
print( "Please enter the name of the city or hometown you grew up in:" ) ;
hometown = input() ;

#3. Ask user for name of pet
print( "\nGreat!\n\nNow enter a pet name, or your pet's name if you have one:" ) ;
pet = input() ;

#4. Combine user inputs to generate new Band Name
print("\nAwesome!\n") ;
print( f"Your band's name should be: The {hometown.title()}-{pet.title()}-Stinkers!\n" ) ;

