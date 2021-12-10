""" Program runs a simple
    Rock, Paper, Scissors
    game that lets the user
    play against their computer.
"""

import random

rock = '''
     _______
 ---'   ____)
       (_____)
       (_____)
       (____)
 ---.__(___)
'''

paper = '''
     _______
 ---'   ____)____
           ______)
           _______)
          _______)
 ---.__________)
'''

scissors = '''
     _____
 ---'   __)______
           ______)
        __________)
       (____)
 ---.__(___)
'''


playing = True ;

print( "\n\n *** ROCK, PAPER, SCISSORS CHALLENGE ***\n\n" ) ;

while(playing):
    
    seed_number = random.randint(0, 1000) ;
    
    random.seed(seed_number) ;
    
    
    computer = random.randint( 0, 2 ) ;
    
    if (computer == 0):
        computer = "rock" ;
        computer_choice = rock ;
    
    elif (computer == 1):
        computer = "paper" ;
        computer_choice = paper ;
    
    else:
        computer = "scissors" ;
        computer_choice = scissors ;
    
    
    response = input(" Type Your Choice [Rock, Paper, Scissors]: ").lower() ;
    
    if (response == "rock"):
        your_choice = rock ;
    
    elif (response == "paper"):
        your_choice = paper ;
    
    else:
        your_choice = scissors ;
    
    
    if ( ((computer == "rock") and (response == "scissors")) or
         ((computer == "paper") and (response == "rock")) or 
         ((computer == "scissors") and (response == "paper")) ):
        print(f"""
{computer_choice}\n\n
 COMPUTER CHOSE:\n\n
{your_choice}\n\n
 YOU CHOSE:\n\n
 YOU LOSE!\n\n
""") ;
    
    
    elif (computer == response):
        print(f"""
{computer_choice}\n\n
 COMPUTER CHOSE:\n\n
{your_choice}\n\n
 YOU CHOSE:\n\n
 DRAW!\n\n
""") ;
    
    
    else:
        print(f"""
{computer_choice}\n\n
 COMPUTER CHOSE:\n\n
{your_choice}\n\n
 YOU CHOSE:\n\n
 YOU WIN!\n\n
""") ;
    
    
    response = input(" Play Again? [Yes, No]: ").lower() ;
    print("\n") ;
    
    if (response == 'no'):
        playing = False ;


print( "\n\n *** THANK YOU FOR PLAYING *** \n\n" ) ;

