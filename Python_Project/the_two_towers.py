from pygame import mixer
import os
from final_scene import final_scene

def the_two_towers():

    input('')
    mixer.init()
    mixer.music.load("./sounds/LOTR - The Majesty of Gondor (soundtrack suite).wav")
    mixer.music.play()

    os.system('clear')

    input("""
Chapter 3: The Two Towers
***  *   *  ** **    **   *  **  *  * * 
   *  *          **    * *        ** * *
    *      *       **       *   *       
  *     *                             * 
                    *                   
*   *      *     *          *   *      *
                                   *    
  
""")
    input("""

Everyone except Gandalf (RIPπͺ¦ ), makes it to the river where they are attacked by a hoard of Uruk-haiπ§ and go their separate ways, thus dissolving the Fellowship of the Ring.
""")

    input("""

Boromir is killed in his fight to protect Merry and Pippin from the Uruk-hai.
π§πΌπͺ¦

Merry and Pippin are taken by the Uruk-hai. 
π§πΌβπΎπ§πΌβπΎπ§

Aragorn, Legolas, and Gimli follow the hoard of Uruk-hai to try to rescue Merry and Pippin.
π§π»ββοΈπ§π»ββοΈπ¨πΎβπ

And Frodo and Sam continue their trek to Mount Doom.
π§π»βπ¦±π¦πΌ
""")

    input("""
Frodo and Sam end up being captured by Faramirπ§π½ββοΈ, son of Denethor who is the Ruling Steward of Gondor.
    """)

    mixer.music.fadeout(10000)

    while True:
        user_choice_4 = input("""
    What happens next: 
    1 - Faramir decides to take Frodo, Sam, and the One Ring to his father, Denethor.
    2 - Faramir sees Frodo's resolve and decides to release him and Sam to continue their journey.
    q- You quit and forsake the peoples of Middle-Earth.
    :""")
        choice_options = ['1', '2','q']
        if user_choice_4 not in choice_options:
            print('\nThat is not a valid option. Please try again.')
            False
        elif user_choice_4 == '1':
            print("""
            
            
Faramir presents his father with the One Ring. Denethor is easily influenced by its evil to return the ring to Sauron.πΉπ Mission failed. Everyone dies. RIP.πͺ¦


""") 
            mixer.music.load("./sounds/Fail - sound effect.wav")
            mixer.music.play()
            input('')
            break
        elif user_choice_4 == '2':
            print('\nFrodo and Sam continue on their seemingly never-ending trek and finally arrive at Mordor. \n\n\t π§π»βπ¦±ππ¦πΌ \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tπ β Mount Doom ')
            final_scene()
            break
        elif user_choice_4 == 'q':
            print('\nSauron thanks you.\n')
            exit()

# the_two_towers()