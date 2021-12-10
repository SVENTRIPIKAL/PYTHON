'''
	Program receives two names via user-input
	and counts the number of times each letter
	from the phrase "true love" appears in each
	name combined; "true" being one set and
	"love" being another set. After each set is
	calculated, the numbers are concatenated
	and converted into an integer, and a
	compatibility score is output to the screen.
'''

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


total_1 = 0 ;                   total_2 = 0 ;

name1 = name1.lower() ;         name2 = name2.lower() ;

total_1 += name1.count('t') ;   total_1 += name2.count('t') ;
total_1 += name1.count('r') ;   total_1 += name2.count('r') ;
total_1 += name1.count('u') ;   total_1 += name2.count('u') ;
total_1 += name1.count('e') ;   total_1 += name2.count('e') ;

total_2 += name1.count('l') ;   total_2 += name2.count('l') ;
total_2 += name1.count('o') ;   total_2 += name2.count('o') ;
total_2 += name1.count('v') ;   total_2 += name2.count('v') ;
total_2 += name1.count('e') ;   total_2 += name2.count('e') ;


score = int(f"{total_1}{total_2}") ;


if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.") ;

elif (score > 40) and (score < 50):
    print(f"Your score is {score}, you are alright together.") ;

else:
    print(f"Your score is {score}.") ;

