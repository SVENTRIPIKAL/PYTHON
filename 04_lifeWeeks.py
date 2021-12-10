"""
    Program receives user's current age
    and calcualtes the remaining days,
    weeks, and months until their 90th
    birthday.
"""


age = input("What is your current age?")

age = int(age) ;    age = ( 90 - age ) ;

days = ( age * 365 ) ;
weeks = ( age * 52 ) ;
months = ( age * 12 ) ;

print( f" You have {days} days, {weeks} weeks, and {months} months left." ) ;

