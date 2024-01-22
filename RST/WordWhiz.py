# Ayden and Chris 
# 2024-01-16
#RST - WordWhiz 
# Google Doc Plan Link - https://docs.google.com/document/d/15WD1waABIEiX8AriV9lAoEK0PrX8HXSUzPiqGPWieFg/edit?usp=sharing

import random

wordle_points = 0
Unscramble_points = 0
scramble = ''
lives = 3

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

def Wordle():
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
    wordle_word = random.choice(wordle_list).upper()
    global wordle_points
    for wordle_num in range(1, 8):
        wordle_guess = input(f"\nGuess {wordle_num}: ").upper()
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

        correct_letters = {
            letter for letter, correct in zip(wordle_guess, wordle_word) if letter == correct
    }
        misplaced_letters = set(wordle_guess) & set(wordle_word) - correct_letters
        wrong_letters = set(wordle_guess) - set(wordle_word)

        print("Correct letters:", ", ".join(sorted(correct_letters)))
        print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
        print("Wrong letters:", ", ".join(sorted(wrong_letters)))

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
    global lives
    lives = 3
    global Unscramble_points
    print('Welcome to Unscramble')
    while lives != 0: 
        unscramble_word = random.choice(unscramble_list)
        scrambled_word = ' '.join(random.sample(unscramble_word, len(unscramble_word)))
        print('')
        print('Here are your letters try to organize them into a word:')
        print('')
        print(scrambled_word)
        print('')
        guess = input('Unscramble the letters into a word:')
        if unscramble_word == guess:
            Unscramble_points +=1
            print('That is correct')  
        else:
            lives -= 1
            print('Incorrect! you have', lives,'lives left!')
            print('The word was',unscramble_word)

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
Which_game = input("What game would you like to play? Type '1' for wordle, '2' for unscramble: ")

if Which_game == '1':
    Wordle()
    
elif Which_game == '2':
    Unscramble()

else:
    print('Not a valid game option, restart and try again.')