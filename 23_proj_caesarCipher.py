"""
    Program Encrypts/Decrypts
    user-input messages. 
    'Encryptions' shift letters to
    the Right according to the 
    amount of shift, and 'Decryptions'
    shift letters back to the Left--
    shift directions continue indefinitely.
"""


def promptResponse():
    return input("\n TYPE 'ENCODE' TO ENCRYPT OR 'DECODE' TO DECRYPT: ").lower() ;


def promptCryption():
    global response ;
    
    if (response == 'encode'):
        return input("\n TYPE A MESSAGE TO ENCRYPT: ").lower() ;
    else:
        return input("\n PASTE AN ENCRYPTED MESSAGE TO DECRYPT: ").lower() ;


def promptShiftNumber():
    return int( input("\n ENTER YOUR ENCRYPTION SHIFT NUMBER: ") ) ;


def encryptDecrypt():
    global alphabet, message, shift, response ;
    
    encryption = "" ;
    
    for letter in message:
        if (not letter.isalpha()):
            encryption += letter ;
        elif (letter.isalpha()):
            index = 0 ;
            for alpha in alphabet:
                if (alpha == letter):
                    break ;
                else:
                    index += 1 ;
            if (response == 'encode'):
                if ( (index + shift) >= len(alphabet) ):
                    difference = ( (index + shift) - len(alphabet) ) ;
                    while ( difference >= len(alphabet) ):
                        difference -= len(alphabet) ;
                    encryption += alphabet[difference] ;
                else:
                    encryption += alphabet[index + shift] ;
            else:
                if ( (index - shift) < 0 ):
                    difference = ( len(alphabet) + (index - shift) ) ;
                    while ( difference < 0 ):
                        difference += len(alphabet) ;
                    encryption += alphabet[difference] ;
                else:
                    encryption += alphabet[index - shift] ;
    
    message = encryption ;


def rePrompt():
    global response, running ;
    
    temp = input(" ENCRYPT OR DECRYPT AGAIN? [ YES | NO ]: ").lower() ;
    
    while ( (temp != 'yes') and (temp != 'no') ):
        print("\n\n INVALID ENTRY!\n\n") ;
        temp = input(" ENCRYPT OR DECRYPT AGAIN? [ YES | NO ]: ").lower() ;
        print() ;
    
    if (temp == 'yes'):
        response = promptResponse() ;
    
    else:
        running = False ;
        print("\n\n\t\t *** EXITING CAESAR CIPHER ***\n ") ;



alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z' ] ;


print("\n\t\t *** WELCOME TO CAESAR CIPHER ***\n ") ;

running = True ;        response = promptResponse() ;

while (running):
    
    if ( (response == 'encode') or (response == 'decode') ):
        message = promptCryption() ;    shift = promptShiftNumber() ;
        encryptDecrypt() ;
        print(f"\n\n {response.upper()}D MESSAGE:\t\t{message.title()}\n\n") ;
        rePrompt() ;
    
    else:
        print("\n\n INVALID ENTRY!\n") ;
        response = promptResponse() ;

