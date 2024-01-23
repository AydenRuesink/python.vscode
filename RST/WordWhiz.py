# Ayden and Chris 
# 2024-01-16
#RST - WordWhiz 
# Google Doc Plan Link - https://docs.google.com/document/d/15WD1waABIEiX8AriV9lAoEK0PrX8HXSUzPiqGPWieFg/edit?usp=sharing

import random #Allows random to be used

#Outlines the points and scores beforehand
wordle_points = 0
Unscramble_points = 0
scramble = ''
lives = 3

#Lists of words that are used in wordle 
wordle_list = [
    "apple", "happy", "table", "music", "water",
    "bread", "house", "chair", "earth", "dream",
    "cloud", "grass", "smile", "plant", "ocean",
    "sunny", "stone", "night", "sugar", "heart",
    "faith", "laugh", "peace", "magic", "light",
    "amber", "lucky", "grape", "fairy", "wrist",
    "frost", "swing", "spark", "blend", "brush",
    "sound", "flame", "dance", "sweet", "shine",
    "charm", "coast", "globe", "fresh", "grain",
    "honey", "melon", "power", "music", "spoon",
    "trunk", "feast", "quest", "crown", "juice",
    "shark", "clock", "lemon", "grind", "slide",
    "sweep", "storm", "tiara", "prize", "waste",
    "swirl", "scent", "scary", "frost", "foggy",
    "dream", "crisp", "creek", "weave", "brave",
    "plaid", "tramp", "crane", "raise", "frost",
    "tulip", "roast", "sweat", "glove", "vivid",
    "graze", "flint", "pride", "fleet", "cabin",
    "bloom", "beard", "greet", "grace", "mirth"
]

#Lists of words that are used in Unscrambled
unscramble_list = [
    "apple", "happy", "table", "cloud", "dream", "python", "guitar", "planet", "orange", "puzzle",
    "river", "zebra", "dance", "magic", "flower", "ocean", "jungle", "sunset", "coffee", "piano",
    "robot", "music", "sunny", "breeze", "cherry", "rocket", "mirror", "silky", "summer", "butter",
    "garden", "whale", "rabbit", "flame", "candle", "shadow", "triple", "mango", "secret", "spirit",
    "freedom", "giraffe", "castle", "voyage", "golden", "whisper", "diamond", "rainbow", "wonder",
    "harmony", "passion", "cosmic", "emerald", "fragile", "paradise", "serene", "journey", "ripple",
    "laughter", "sapphire", "serpent", "illusion", "stellar", "heavenly", "mystic", "charming", "stellar",
    "tranquil", "cascade", "infinity", "lagoon", "mystery", "sparkle", "radiant", "vivid", "solitude",
    "courage", "fountain", "lullaby", "whimsical", "cypress", "velvet", "enigma", "lunar", "enchant",
    "brilliant", "twilight", "marvel", "ethereal", "gentle", "echo", "rhapsody", "luminary", "mesmerize"
]

#Creates a function named wordle so it is easy to call back to and re-write
def Wordle():
    #Talks about the game rules
    print('')
    print('Welcome to Wordle')
    print('')
    print('How to play:')
    print('1. Your objective is to guess the five letter word within 6 tries.')
    print('2. When guessing a word, there are three options that will appear:')
    print(' 2a. Correct letters: Meaning that the letter is in the correct position')
    print(' 2b. Misplaced letters: Meaning that the letter is in the word but in the wrong position')
    print(' 2c. Incorrect letters: The letters are not using iin the word')
    print('3. Have fun and good luck!!!!')

    #Picks a word from the list
    wordle_word = random.choice(wordle_list).upper()

    #Allows wordle_points to be changed within the variable 
    global wordle_points
    
    #the code will run 6 times, indicating the amount of guesses they have
    for wordle_num in range(1, 7):
        #Asks the user for their guess
        wordle_guess = input(f"\nGuess {wordle_num}: ").upper()
        #If the guess is correct the game ends and the user gets to choose if they want to play again, switch games, or stop playing  
        if wordle_guess == wordle_word:
            print("Correct")
            wordle_points = wordle_points + 1
            wordle_again = input('Do you want to play again? 1 for yes, 2 for no: ')
            if wordle_again == '1':
                Wordle()
            elif wordle_again == '2':
                print('You earned',str(wordle_points),'points.')
                wordle_points = 0 
                change_game = input('Would you like to switch games? 1 for yes, 2 for no: ')
                if change_game == '1':
                    Unscramble()
                else:
                    print('Thanks for Playing!!!')
            else:
                print('Not a valid Answer!!') 
            break
            #Variable finds the correct letters by comparing it with zip
        if len(wordle_guess) > 5:
            print("Too many letters, you just lost a life, try to input a 5 letter word next time")
        else:
            correct_letters = {
                letter for letter, correct in zip(wordle_guess, wordle_word) if letter == correct
    }
        #Finds misplaced letters
            misplaced_letters = set(wordle_guess) & set(wordle_word) - correct_letters
        #Finds wrong letters
            wrong_letters = set(wordle_guess) - set(wordle_word)
        
        #displays the letter placement 
            print("Correct letters:", ", ".join(sorted(correct_letters)))
            print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
            print("Wrong letters:", ", ".join(sorted(wrong_letters)))

        #If after 6 tries the user does not get the word it displays an output 
            if wordle_num == 6:
                print('Sorry you lost')
                print('The word was',wordle_word)
                print('\n')
                wordle_again = input('Do you want to play again? 1 for yes, 2 for no: ')
                if wordle_again == '1':
                    Wordle()
                elif wordle_again == '2':
                    print('You earned',str(wordle_points),'points.')
                    wordle_points = 0 
                    change_game = input('Would you like to switch games? 1 for yes, 2 for no: ')
                    if change_game == '1':
                        Unscramble()
                    else:
                        print('Thanks for Playing!!!')
                else:
                    print('Not a valid Answer!!')
                break
    
def Unscramble():
    #Allows lives to be manipulated in def
    global lives
    lives = 3
    global Unscramble_points
    print('Welcome to Unscramble')
    while lives != 0: 
        #Picks a word from the list
        unscramble_word = random.choice(unscramble_list)
        #scrambles the unscrambled_word using len 
        scrambled_word = ' '.join(random.sample(unscramble_word, len(unscramble_word)))
        print('')
        print('Here are your letters try to organize them into a word:')
        print('')
         #This gives the user the actual unscrambled word
        print(scrambled_word)
        print('')
        #Asks user for input
        guess = input('Unscramble the letters into a word:')
        #If correct it adds a life
        if unscramble_word == guess:
            Unscramble_points +=1
            print('That is correct')  
        #If incorrect it takes away a life
        else:
            lives -= 1
            print('Incorrect! you have', lives,'lives left!')
            #Gives the user the correct answer
            print('The word was',unscramble_word)
    #Asks user for input
    unscramble_again = input('Do you want to play again? 1 for yes, 2 for no: ')
    if unscramble_again == '1':
        Unscramble()
    elif unscramble_again == '2':
        print('You earned',str(Unscramble_points),'points.')
        Unscramble_points = 0 
        change_game = input('Would you like to switch games? 1 for yes, 2 for no: ')
        if change_game == '1':
            Wordle()
        else:
            print('Thanks for Playing!!!')
    else:
        print('Not a valid Answer!!') 
        
    
print('')
print('Welcome to WordWhiz')
print('\n')
#Asks user for input on which game they would like to play
Which_game = input("What game would you like to play? Type '1' for wordle, '2' for unscramble: ")

# if input is 1 the variable wordle is called
if Which_game == '1':
    Wordle()

#If input is 2 the variable unscrambled is called    
elif Which_game == '2':
    Unscramble()

else:
    print('Not a valid game option, restart and try again.')