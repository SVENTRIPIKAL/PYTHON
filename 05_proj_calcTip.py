"""
    Simple program works as a tip calculator
    by receiving total bill, tip percentage,
    and number of payees to calculate
    individual tip amounts.
"""

#1. Introduce program
print( "\nTHIS IS A TIP CALCULATOR!\n" ) ;


#2. receive user-input: total bill
bill = float( input( "What is your total bill? $" ) ) ;
print("\nOkay!\n") ;


#3. receive user-input: tip percentage
print( "What percent of tip will you be leaving?" ) ;
percentage = int( input( "[ 10, 12, or 15 ]: " ) ) ;
percentage = ( percentage / 100 ) ;
print("\nNice!\n") ;


#4. receive user-input: number of payees
payees = int( input( "How many people will be splitting the bill? " ) ) ;
print("\nSuper!\n") ;

#5. calculate tip
percentage = ( bill * percentage ) ;  # calculate percentage according to bill

bill = ( bill + percentage ) ;        # add percentage amount to total bill

tip = round( (bill / payees), 2) ;    # calculate tip rounded 2 decimals

#6. output individual tip amounts
if payees > 1:
    print( f"Each person will be paying: ${tip:.2f}\n" ) ;
else:
    print( f"Total due: ${tip:.2f}\n" ) ;
