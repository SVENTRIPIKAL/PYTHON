"""
	Program initializes a 
	mini-game of HANGMAN.
"""


import random                           # allows use of random functions

seed_num = random.randint(1, 1000) ;    # draws a random seed number

random.seed(seed_num) ;                 # creates random seed


logo = """
\t\t ===================================================
\t\t =  _                                              =
\t\t = | |                                             =
\t\t = | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   =
\t\t = | '_  \/ _` | '_  \/ _` | '_ ` _ \ / _` | '_  \ =
\t\t = | | | | (_| | | | | (_| | | | | | | (_| | | | | =
\t\t = |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| =
\t\t =                     __/ |                       =
\t\t =                    |___ /                       =
\t\t ===================================================
"""

                                    # beginning output
start = """
  ___________.._______
 | .__________))______|
 | | / /      ||
 | |/ /       ||
 | | /        ||
 | |/         ||
 | |          ||
 | |          '.
 | |          
 | |          
 | |          
 | |          
 | |          
 | |          
 | |          
 | |          
 | |          
 | |          
 ''''''''''|=========|'''|
 |'|--------=========''|'|
 | |                   | |
 : :                   : :
 ._.                   ._.
"""

                                    # head output
head = """
  ___________.._______
 | .__________))______|
 | | / /      ||
 | |/ /       ||
 | | /        ||.-''.
 | |/         |/  _  \\
 | |          ||  `/,|
 | |          (\\\`_.'
 | |           `--'
 | |          
 | |          
 | |          
 | |          
 | |          
 | |          
 | |          
 | |          
 | |          
 ''''''''''|=========|'''|
 |'|--------=========''|'|
 | |                   | |
 : :                   : :
 ._.                   ._.
"""

                                    # body output
body = """
  ___________.._______
 | .__________))______|
 | | / /      ||
 | |/ /       ||
 | | /        ||.-''.
 | |/         |/  _  \\
 | |          ||  `/,|
 | |          (\\\`_.'
 | |         .-`--'.
 | |         \ . . /
 | |          |   | 
 | |          | . | 
 | |          |___| 
 | |          
 | |          
 | |          
 | |          
 | |          
 ''''''''''|=========|'''|
 |'|--------=========''|'|
 | |                   | |
 : :                   : :
 ._.                   ._.
"""

                                    # additional arm output
arm_1 = """
  ___________.._______
 | .__________))______|
 | | / /      ||
 | |/ /       ||
 | | /        ||.-''.
 | |/         |/  _  \\
 | |          ||  `/,|
 | |          (\\\`_.'
 | |         .-`--'.
 | |        /Y . . /
 | |       // |   | 
 | |      //  | . | 
 | |     ')   |___| 
 | |          
 | |          
 | |          
 | |          
 | |          
 ''''''''''|=========|'''|
 |'|--------=========''|'|
 | |                   | |
 : :                   : :
 ._.                   ._.
"""

                                    # additional arm output
arm_2 = """
  ___________.._______
 | .__________))______|
 | | / /      ||
 | |/ /       ||
 | | /        ||.-''.
 | |/         |/  _  \\
 | |          ||  `/,|
 | |          (\\\`_.'
 | |         .-`--'.
 | |        /Y . . Y\\
 | |       // |   | \\\\
 | |      //  | . |  \\\\
 | |     ')   |___|   (`
 | |          
 | |          
 | |          
 | |          
 | |          
 ''''''''''|=========|'''|
 |'|--------=========''|'|
 | |                   | |
 : :                   : :
 ._.                   ._.
"""

                                    # additional leg output
leg_1 = """
  ___________.._______
 | .__________))______|
 | | / /      ||
 | |/ /       ||
 | | /        ||.-''.
 | |/         |/  _  \\
 | |          ||  `/,|
 | |          (\\\`_.'
 | |         .-`--'.
 | |        /Y . . Y\\
 | |       // |   | \\\\
 | |      //  | . |  \\\\
 | |     ')   |___|   (`
 | |          || 
 | |          || 
 | |          || 
 | |          || 
 | |         / | 
 ''''''''''|=`-'=====|'''|
 |'|--------=========''|'|
 | |                   | |
 : :                   : :
 ._.                   ._.
"""

                                    # additional leg output
leg_2 = """
  ___________.._______
 | .__________))______|
 | | / /      ||
 | |/ /       ||
 | | /        ||.-''.
 | |/         |/  _  \\
 | |          ||  `/,|
 | |          (\\\`_.'
 | |         .-`--'.
 | |        /Y . . Y\\
 | |       // |   | \\\\
 | |      //  | . |  \\\\
 | |     ')   |___|   (`
 | |          || ||
 | |          || ||
 | |          || ||
 | |          || ||
 | |         / | | \\
 ''''''''''|=`-'==`-'|'''|
 |'|--------=========''|'|
 | |                   | |
 : :                   : :
 ._.                   ._.
"""

                                    # losing game output
lose ="""
  ___________.._______
 | .__________))______|
 | | / /      ||
 | |/ /       ||
 | | /        ||.-''.
 | |/         |/  _  \\
 | |          ||  X/x|
 | |          (\\\`O .'
 | |         .-`--'.
 | |        /Y . . Y\\
 | |       // |   | \\\\
 | |      //  | . |  \\\\
 | |     ')   |___|   (`
 | |          || ||
 | |          || ||
 | |          || ||
 | |          || ||
 | |         / | | \\
 ''''''''''|_`-'  `-'|'''|
 |'|-------\ \       ''|'|
 | |        \ \        | |
 : :         \ \       : :
 ._.          `'       ._.
"""


hangman = [ start, head, body, arm_1,           # list holds hangman outputs
            arm_2, leg_1, leg_2, lose ] ;

letters = [ 'A', 'B', 'C', 'D', 'E', 'F',       # list holds all game letters
            'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z' ] ;

quotes = [ "Go Harder Than Last Time!",         # list holds all game quotes
           "Oh, Happy Days...", 
           "To Be, Or Not To Be.",
           "I Am Sam...Sam I Am." ] ;



def listQuote( phrase ):        # function receives a quote and updates
    global quoted_list ;        # a list to store letters from quote--
                                # does not store duplicates.
    for i in phrase:
        if ( (i.isalpha()) and (i.lower() not in quoted_list) ):
            quoted_list.append(i.lower()) ;

def hideQuote( phrase ):        # function receives a quote and creates
    temp = "" ;                 # a string of horizontal lines for each
    for index in phrase:        # letter in a quote--returns the string
        if (index == " "):      # for output.
            temp += " " ;
        elif (index.isalpha()):
            temp += "_ "
        else:
            temp += f"{index} " ;
    return temp ;

def checkGuess( guess, phrase ):             # function checks if a letter
    global correct, tries, correct_guesses ; # exists in the original quote
                                             # and updates user tries, guesses
    if (guess.lower() in phrase.lower()):    # and correct attempts accordingly.
        correct = True ;
        if (guess.lower() not in correct_guesses):
            correct_guesses.append( guess.lower() ) ;
    
    else:
        tries += 1 ;

def updateHidden( phrase ): 
    global correct_guesses ;    temp = "" ;  # function works the same as
                                             # the hideQuote() function except
    for index in phrase:                     # it updates the string with
        if (index == " "):                   # letters that have been correctly
            temp += " " ;                    # guessed--returns the string.
        elif ( (index.isalpha()) and (index.lower() in correct_guesses) ):
            temp += f"{index} "
        elif ( (index.isalpha()) and (index.lower() not in correct_guesses) ):
            temp += "_ "
        else:
            temp += f"{index} " ;
    
    return temp ;

def promptReplay():                                 # function prompts user for
    global playing, correct_guesses, quoted_list ;  # a new game, and updates
    global tries, phrase, hiddenQuote ;             # variables accordlingly.
    
    response = input(" Would You Like To Play Again? ") ;
    
    if (response.lower() == 'no'):
        playing = False ;
        printLines(50) ;
    
    else:
        correct_guesses = [] ;      quoted_list = [] ;   tries = 0 ;
        printLines(10) ;            print(logo) ;        print( hangman[tries] ) ;
        random.shuffle(quotes) ;    phrase = random.choice(quotes) ;
        listQuote(phrase) ;         hiddenQuote = hideQuote(phrase) ;

def printLines( number ):       # function prints specified
    for i in range(number):     # number of New Lines
        print() ;



correct_guesses = [] ;      quoted_list = [] ;      tries = 0 ;
playing = True ;            print(logo) ;           print( hangman[tries] ) ;
random.shuffle(quotes) ;    phrase = random.choice(quotes) ;
listQuote(phrase) ;         hiddenQuote = hideQuote(phrase) ;


while (playing):
    
    if ( tries == 7 ):
        print("\n\n\t   YOU LOSE! \n\n") ;
        
        promptReplay() ;
    
    elif ( sorted(correct_guesses) == sorted(quoted_list) ):
        print(f"\n\n\t   YOU WIN! \t\t\t\"{phrase.title()}\"\n\n") ;
        
        promptReplay() ;
    
    else:
        correct = False ;        print(f"\t\t\t      {hiddenQuote}") ;
        
        guess = input(f"\n\n     GUESS A LETTER: " ) ;
        
        printLines(10) ;         print(logo) ;
        
        checkGuess( guess, phrase ) ;       print( hangman[tries] ) ;
        
        hiddenQuote = updateHidden( phrase ) ;



print("\t\t\t     *** THANK YOU FOR PLAYING *** \n\n") ;

