""" short narrative-driven user-interactive
    game where the user must correctly
    navigate through a story to reach the
    famous Treaure Island treasure chest.
"""

print(
        """
   ,d                                                                        
   88                                                                      
 MM88MMM 8b,dYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88     88 8b,dYba, ,adPPYba,
   88    88P' "Y8 a8P_____88 ""     `Y8 I8[    "" 88     88 88P' "Y8 a8P_____88
   88    88       8PP''''''' ,adPPPPP88  `"Y8ba,  88     88 88       8PP"""""""
   88,   88       "8b,   ,aa 88,    ,88 aa    ]8I "8a, ,a88 88       "8b,   ,aa
   "Y888 88        `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YdP'Y8 88        `"Ybbd8"'
   
              ""           88                               88 
              ""           88                               88 
                           88                               88 
              88 ,adPPYba, 88 ,adPPYYba, 8b,dYba,   ,adPPYb,88 
              88 I8[    "" 88 ""     `Y8 88P' `"8a a8"    `Y88 
              88  `"Y8ba,  88 ,adPPPPP88 88     88 8b       88 
              88 aa    ]8I 88 88,    ,88 88     88 "8a,   ,d88 
              88 `"YbbdP"' 88 `"8bbdP"Y8 88     88  `"8bbdP"Y8 
    
                          ____...------------...____
                     _.-"` /o/__ __ __ __ __  _ \o\ `"-._
                   .'     / /                    \ \     '.
                   |=====/o/======================\o\=====|
                   |____/_/________..____..________\_\____|
                   /   _/ \_     <_o#\__/#o_>     _/ \_   \\
                   \\________________\####/________________/
                    |===\!/==========v==v==========\!/===|
                    |   |=|          .---.         |=|   |
                    |===|o|=========/     \========|o|===|
                    |   | |         \() ()/        | |   |
                    |===|o|======{'-.) U (.-'}=====|o|===|
                    | __/ \__     '-.\\vvv/.-'    __/ \__ |
                    |          ====.'.'^'.'.====         |
                    |_ _\o/_ ___  {.' ___ '.} ___ _\o/_ _|
                    `_/  '                          `  \\_'
        \n\n\n"""
) ;

print(""" \t\t Welcome to Treasure Island!\n
          Your mission is to find the Lost Treasure\n
          by navigating through the story successfully.\n\n
      """)

response = input("Type 'Start' to Start The Game or 'Exit' to End: ").lower() ;

if (response == 'start'):
    
    playing = True ;
    

else:
    
    playing = False ;
    

while ( playing ):
    
    print("""     \n\n\t          Following a treasure map \n
                  you bought from a local \n
                  merchant for three shillings, \n
                  you begin your journey at \n
                  a corridor with only two \n
                  directions to choose from: \n\n
          """) ;
    response = input(" Will you go Left or Right? [Left | Right]: ").lower() ;
    
    if (response == 'left'):
        print(""" \n\n\t\t  You turn left and journey forth \n
                  for three hours until you come \n
                  to a large murky lake which blocks \n
                  your path. \n
              """) ;
        response = input(" Will you swim across or wait? [Swim | Wait]: ").lower() ;
    
    else:
        print( "\n\n You turn right to only be mauled by a Three-Headed Dragon! \n\n" ) ;
        print(" GAME OVER! \n\n") ;
        response = input(" Would you like to play again? [Yes | No]: ").lower() ;
        if (response == 'no'):
            playing = False ;
        continue ;
    
    
    
    if (response == 'swim'):
        print(""" \n\n\t\t  With nothing to lose, you jump into \n
                  the lake only to find it is but chest \n
                  high. Aside from having yourself and \n
                  your belongings soaked, you successfully \n
                  cross the lake unscathed. You head East \n
                  towards a desserted town marked on the \n
                  map as the journey's final destination. \n
                  Upon arrival, you stand before three \n
                  mysterious doors of different colors: \n\n
              """) ;
        response = input(" Which will you open? [Red | Blue | Yellow]: ").lower() ;
    
    else:
        print(""" \n\n\t\t You wait for a minute in the hopes \n
                  a ship would arrive to carry you \n
                  safely across, but notice night has \n
                  fallen. You ultimately find yourself \n
                  surrounded by a pack of hungry wolves \n
                  and are mauled to death. \n\n
              """) ;
        print(" GAME OVER! \n\n") ;
        response = input(" Would you like to play again? [Yes | No]: ").lower() ;
        if (response == 'no'):
            playing = False ;
        continue ;
    
    
    if (response == 'red'):
        print(""" \n\n\t\t  You open the door to find the large and \n
                  heavy chest of Treasure Island -- over \n
                  flowing with gems, gold, rubies, and more! \n
                  Despite how rich you have just become, the \n
                  only predicament you find yourself in now is \n
                  deciding just how you will carry it home... \n\n
              """) ;
        print(" YOU WIN! \n\n") ;
        response = input(" Would you like to play again? [Yes | No]: ").lower() ;
        if (response == 'no'):
            playing = False ;
        continue ;
    
    else:
        print(""" \n\n\t\t You open the door and are \n
                  immediately attacked by carnivorous \n
                  trolls! \n\n
              """) ;
        print(" GAME OVER! \n\n") ;
        response = input(" Would you like to play again? [Yes | No]: ").lower() ;
        if (response == 'no'):
            playing = False ;
        continue ;




print("\n\n THANK YOU FOR PLAYING!\n\n") ;

