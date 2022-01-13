"""
    Program Encrypts/Decrypts
    user-input messages. 
    'Encryptions' shift letters to
    the Right according to the 
    amount of shift, and 'Decryptions'
    shift letters back to the Left--
    shift directions continue indefinitely.
"""



logo = """           
             ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
            a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
            8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
            "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
             `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
             
                       88             88                                 
                       ""             88                                 
                                      88                                 
             ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
            a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
            8b         88 88       d8 88       88 8PP""""""" 88          
            "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
             `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                          88                                             
                          88           
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
        print("\n\n\t\t\t    *** EXITING CAESAR CIPHER ***\n ") ;



alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z' ] ;


print(f"\n{logo} ") ;

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

