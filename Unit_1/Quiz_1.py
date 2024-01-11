#Ayden Ruesink
#2024-01-09

#Sets marks to zero
marks = 0

print('Welcome to the Quiz')
print('')
print('This is worth a 100% of your final grade, please read everything clearly before answering')

print('\n')

print('Question 1')
print('')
print('If I have six eggs, I take 2, cook 2, and eat 2, how many eggs do I have left?')

print('a) 2')
print('b) 5')
print('c) 0')
print('d) 12')
print('e) 4')

#Collects users answer
answer1 = input('Answer: ')

#Converts their answer into lowercase so it can be used in the if statement even if user inputs uppercases
answer1 = answer1.lower()

#If the answer is correct it adds a point and gives a thumbs up
if answer1 == 'e':
    marks +=1
    print('✅ 😊')
#If the answer is wrong it gives an x and the correct answer
else:
    print('❌ 😞 ')
    print('The correct answer was: e')
    
print('\n')

print('Question 2')
print('')
print('How many planets are in our solar system?')

print('a) 9')
print('b) 8')
print('c) 2')
print('d) 14')
print('e) 144')

#Collects users answer
answer2 = input('Answer: ')

#Converts their answer into lowercase so it can be used in the if statement even if user inputs uppercases
answer2 = answer2.lower()

#If the answer is correct it adds a point and gives a thumbs up
if answer2 == 'b':
    marks +=1
    print('✅ 😊')
else:
#If the answer is wrong it gives an x and the correct answer
    print('❌ 😞 ')
    print('The correct answer was: b')
    
print('\n')

print('Question 3')
print('')
print('What is the name of the Canadian dish that fundamentally consists of fries, gravy, and cheese curds?')

#Collects users answer
answer3 = input('Answer: ')

#Converts their answer into lowercase so it can be used in the if statement even if user inputs uppercases
answer3 = answer3.lower()

#If the answer is correct it adds a point and gives a thumbs up
if answer3 == 'poutine':
    marks +=1
    print('✅ 😊')
else:
#If the answer is wrong it gives an x and the correct answer
    print('❌ 😞 ')
    print('The correct answer was: poutine')
    
print('\n')

print('Question 4')
print('')
print('If you have six apples and I take away 4 how many apples do you now have in total?')

print('a) 9')
print('b) 8')
print('c) 2')

#Collects users answer
answer4 = input('Answer: ')

#Converts their answer into lowercase so it can be used in the if statement even if user inputs uppercases
answer4 = answer4.lower()

#If the answer is correct it adds a point and gives a thumbs up
if answer4 == 'c':
    marks +=1
    print('✅ 😊')
else:
#If the answer is wrong it gives an x and the correct answer
    print('❌ 😞 ')
    print('The correct answer was: c')
    
print('\n')

print('Question 5')
print('')
print('What is the highest mountain in the world?')

print('a) Everest')
print('b) Logan')
print('c) K2')
print('d) Kangchenjunga')
print('e) Gasherbrum I')

#Collects users answer
answer5 = input('Answer: ')

#Converts their answer into lowercase so it can be used in the if statement even if user inputs uppercases
answer5 = answer5.lower()

#If the answer is correct it adds a point and gives a thumbs up
if answer5 == 'a':
    marks +=1
    print('✅ 😊')
else:
    print('❌ 😞 ')
    print('The correct answer was: a')
    
print('\n')

#Asks if they want to participate in a bonus question
bonus = input('Bonus question (This will not negatively impact your grade, if you want to take it enter Y if not enter N: ')
bonus = bonus.lower() 

#if they input Y it tells them the question if they don't it moves on
if bonus == 'y':
    print('What is the most played sport in the world: ')
    answer6 = input('Answer: ')
    answer6 = answer6.lower()
    if answer6 == 'soccer':
        marks +=1
        print('✅ 😊')
    else:
        print('❌ 😞 ')
        print('The correct answer was: soccer')


print('\n')
print('Congrats on finishing the quiz!!')

print('')
#Calculates the percentage
percentage = round(marks/5 * 100,ndigits=2)

#Tells their mark out of 5 and gives them the percentage
print('You achieved '+str(marks)+' out of 5, totalling a percentage of '+str(percentage)+'%.')

print('')
#Gives a sentence and emoji bases on their mark
print('Final Comments:')
if marks == 0:
    print('Thats kind of embarrassing. 😤 ')
elif marks == 1: 
    print('You need to Study!!!! 😰 ')
elif marks == 2:
    print('Not the greatest performance.😥')
elif marks == 3: 
    print('I mean at least you passed. 🙁')
elif marks == 4:
    print('SO CLOSEEE!!! 🙂')
elif marks == 5:
    print('100%!!  😊')
else: 
    print('Over 100%, you made it look easy! 😁')