"""
    Program works as a simple
    BMI calculator: dividing
    user's weight in (kg) by the
    user's height in (m) squared.
"""


height = input("enter your height in m: ") ;
weight = input("enter your weight in kg: ") ;

height = float(height) ;   weight = float(weight) ;

bmi = int( weight / (height**2) ) ;

print( bmi ) ;

