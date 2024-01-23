WordWhiz 

Our code is separated into two mini-games: 
1. Wordle
2. Unscramble

WORDLE

Basically, the code takes a random word from the wordle_list and sets it as the user's code to find. 

Using Input statements, the user guesses the wordle_word 

Using Zip command it compares the user's guess to the world_word to see if they match. 

If the user's word is correct, it ends the code and asks the user if they want to play again with the use of an if statement 
1. If yes, the game replays and the user's score is tracked
2. If no, the game ends and asks if the user wants to switch games or log off

With zip and set commands which identify the category of which each letter in the user's word falls, it is able to identify 3 things from the user's guess:
1. correct letter: The letter is in the correct position
2. Misplaced Letter: The letter is in the word but in the wrong position
3. Wrong letter: The letter is not in the word

After 6 guesses if the user is not able to identify the word, the game ends and reveals the wordle_word

At the end, it asks if the user wants to play again, switch games, or completely stop playing. 

UNSCRAMBLE

Basically, the code takes a few letters from a 4 to 10-letter long word from the Unscramble_List and sets it as the user's code to find.

Using string properties, len and random. sample the code scrambles the word for the user to guess

Using input statements, the user guesses the word through the scrambled_word

if the user gets the word, the code resets and another word is shown 

Every time the user gets it wrong -1 lives, once they lose all of their lives the code ends and asks the user if they want to play again with the use of an if statement 
1. If yes, the game replays and the users score is tracked
2. If no, the game ends and asks if the user wants to switch games or log off

The code will go on forever until the user loses all three lives. 

At the end it asks if the user wants to play again, switch games, or completely stop playing. 





